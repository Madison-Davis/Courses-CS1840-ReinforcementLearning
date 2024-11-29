from ase import *
from ase.visualize import *
import numpy
from random import choice
import sys
from .make_basin_move import *
import math
from random import shuffle

def make_ga_move(ratio='',ini_structures='',search_structures='',pool_size=0.1,
	atoms_per_fu='',fu='',vac_ratio='',max_fus='',system_type='',composition='',
	ap='',cubic_solutions='',tetragonal_solutions='',hexagonal_solutions='',
	orthorhombic_solutions='',monoclinic_solutions='',max_atoms='',moves='',max_pool_size=250, no_basin_hopping=False):

	#options should be mate or mutate
	#if mutate, can impliment an random MC move?
	#first need to construct a weighted list between mating & mutating
	weighted_list=[]
	for i in range(len(ratio)):
		for j in range(ratio[i]):
			weighted_list.append(i)
	move=choice(weighted_list)
	
	### first need to create a compiled list of all structures and all energies #
	all_structures=[]
	all_energies=[]
	nstruct=0
	for i in range(len(ini_structures)):
		struct=ini_structures[i+1]
		all_structures.append(struct)
		all_energies.append([struct[-1],nstruct])
		nstruct+=1
		
	for i in range(1,len(search_structures)):
		struct=search_structures[i]
		all_structures.append(struct)
		all_energies.append([struct[-1],nstruct])
		nstruct+=1
	
	#############################################################################
	### now create a mating population ##########################################
	all_energies.sort()
	pool=[]
	cut=int(len(all_energies)*pool_size)
	for i in range(cut):
		pool.append(all_structures[all_energies[i][1]])
	
	
	if cut < 2: ### if starting pool of structures is too small to return a population
		#within the cutoff, use all avalible structures, but still sorted in energy order
		for i in range(len(all_energies)):
			pool.append(all_structures[all_energies[i][1]])
	#############################################################################
	
	### now need to choose some random structures to include in the mating pool #
	runt_pool=len(all_energies)-cut
	runts=all_energies[cut:]
	#choose a number of runts to include in the pool
	try:
		c=choice(list(range(len(runts),int(cut))))
	except:
		c=0
	runt_pool=[]
	for i in range(c):
		temp=choice(runts)
		if temp not in pool:
			pool.append(all_structures[temp[1]])
	
	#############################################################################

	# now clip pool to maximum size if defined / pool larger than limit
	if max_pool_size != '':
		if len(pool) > max_pool_size:
			shuffle(pool)
			del pool[max_pool_size:]
	if move == 0: # mating take two slices from two different structures, combine them
		# & tidy the structure up to make sure the composition is correct & workable
		# assembly instructions
		if len(pool) > 2:
			parent1=choice(pool)
			parent2=choice(pool)
			x=0
			while parent1 == parent2:
				parent2 = choice(pool)
				x+=1
				if x == 150000:
					move=1
					break
			string1=parent1[1]
			string2=parent2[1]
			instructions1=parent1[2]
			instructions2=parent2[2]
			new_string=[]
			slice1=len(string1)
			slice2=len(string2)
			slice1=choice(list(range(0,slice1+1,4))) 
			slice2=choice(list(range(0,slice2+1,4)))
			start1=choice([0,-1])
			start2=choice([0,-1])
			
			string1=string1[start1:slice1]
			string2=string2[start2:slice2]
			for i in range(len(string1)):
				new_string.append(string1[i])
			
			for i in range(len(string2)):
				new_string.append(string2[i])
				
			species=list(set(fu))
			string_composition={}
			for i in range(len(species)):
				string_composition[species[i]]=fu.count(species[i])
			
			new_string_comp={}
			for i in range(len(new_string)):
					if new_string[i] != 0:
						try:
							new_string_comp[new_string[i]]+=1
						except:
							new_string_comp[new_string[i]]=1
			
			if new_string != []:
				if list(set(new_string)) != [0]:
					missing={}
					keys=list(string_composition.keys())
					rats=[]					
					for i in range(len(keys)):
						try:	
							rats.append([new_string_comp[keys[i]]/string_composition[keys[i]],keys[i]])
						except:
							rats.append([0,keys[i]])
					
					target_fus=float(math.ceil(max(rats)[0]))
					for i in range(len(rats)):
						if rats[i][0] != target_fus:
							missing[rats[i][1]]=(target_fus-rats[i][0])
						
					keys=list(missing.keys())
					for i in range(len(keys)):
						missing[keys[i]]=round(missing[keys[i]]*string_composition[keys[i]])
					#now need to make sub module(s) from the atoms that need to be added in
					new_mods=[]
					for i in range(len(keys)):
						for j in range(missing[keys[i]]):
							new_mods.append(keys[i])
					#need to find out how many zeros the string needs to be padded with
					
					if system_type=='neutral':
						#print(new_mods)
						for i in range(4-(len(new_mods) % 4)):
							new_mods.append(120)
						#print(new_mods)
						
					if system_type=='ionic':
						cats=[]
						symbols=list(composition.keys())
						for i in range(len(symbols)):
							temp=Atoms(symbols[i])
							if composition[symbols[i]][1] > 0:
								cats.append(list(temp.get_atomic_numbers())[0])
						As=[] #cations 
						Bs=[] #everything else
						for i in range(len(new_mods)):
							if new_mods[i] in cats:
								As.append(new_mods[i])
							else:
								Bs.append(new_mods[i])
						
						required=(len(As)*4)-len(As)-len(Bs)
						
						for i in range(required):
							Bs.append(120)
						
						shuffle(Bs)
						new_sub_mods=[]
						for i in range(len(As)):
							new_sub_mods.append(As[i])
							for j in range(3):
								new_sub_mods.append(Bs[-1])
								del Bs[-1]
						
						#choose position to insert into the new_string & insert any new submods
						insert=choice(list(range(0,len(new_string),4)))
						temp1=new_string[0:insert]
						for i in range(len(new_sub_mods)):
							temp1.append(new_sub_mods[i])
						for i in range(len(new_string[insert:])):
							temp1.append(new_string[i+insert])
						new_string=temp1
						
						# now workk out if we can use either parents instructions, if not
						# create new random ones
						options=[0,0]
						if len(new_string) == len(parent1[1]):
							options[0]=1
							
						if len(new_string) == len(parent2[1]):
							options[1]=1
						
						if options.count(0) == 2:
							try:
								new_instructions=create_random_instructions(new_string,ap,cubic_solutions,tetragonal_solutions,hexagonal_solutions,orthorhombic_solutions,monoclinic_solutions,instructions)
							except:
								instructions = []
								new_instructions=create_random_instructions(new_string,ap,cubic_solutions,tetragonal_solutions,hexagonal_solutions,orthorhombic_solutions,monoclinic_solutions,instructions)
								
							
						if options.count(0) == 1:
							if options[0] == 1:
								new_instructions=parent1[2]
							if options[1] == 1:
								new_instructions=parent2[2]
						
						if options.count(0) == 0:
							temp1=choice([0,1])
							if temp1 == 0:
								new_instructions=parent1[2]
							if temp1 == 1:
								new_instructions=parent2[2]
						
						#print("instructions",new_instructions)
						#print("options", options)
						
						try:
							atoms,new_instructions=assemble_structure(new_string,new_instructions)
							new_structure=[atoms,new_string,new_instructions]
						except:
							atoms=None
							new_structure=[atoms,new_string,new_instructions]

				else:
					move = 1
					
			else:
				move=1
			
		else:
			move =1
	
	if move == 1: # mutation: select a structure from the pool & apply a basin hopping move

		if no_basin_hopping:
			return

		current_structure=choice(pool)
#		moves={1:1,2:1,3:1,4:1,5:1,6:1,7:1}
		# if moves == None:
		# 	moves={1:1}
		# else:
		# 	moves[8]=0
		moves = {1: 1}
		from fuse_rl.make_basin_move import make_basin_move
		new_structure=make_basin_move(current_structure,atoms_per_fu,fu,vac_ratio,max_fus,system_type,composition,ap,cubic_solutions,tetragonal_solutions,hexagonal_solutions,orthorhombic_solutions,monoclinic_solutions,moves=moves,max_atoms=max_atoms)
		
	return new_structure
	
