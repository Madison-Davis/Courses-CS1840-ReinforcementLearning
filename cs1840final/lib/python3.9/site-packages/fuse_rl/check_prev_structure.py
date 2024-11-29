import spglib
from ase.build import sort
import sys
from ase.visualize import *
def check_prev_structure(atoms,prev_start_points):
	try:
		sort(atoms)
		shift=[-atoms[0].position[0],-atoms[0].position[1],-atoms[0].position[2]]
		atoms.translate(shift)
		std_cell=spglib.standardize_cell(atoms,to_primitive=True,symprec=1e-4)
	except:
		check = None
		return check
	try:
		current_cell=std_cell[0]
		current_positions=std_cell[1]
		current_species=std_cell[2]
	except:
		check=None
		return check
	#print(prev_start_points)
	cells=[]
	positions=[]
	species=[]
	test1=False
	test2=False
	test3=False
	check = False
	
	for i in range(len(prev_start_points)):
		cells.append(prev_start_points[i][0])
		positions.append(prev_start_points[i][1])
		species.append(prev_start_points[i][2])
	
	#print ("cell 1:")
	#print(current_cell)
	#print ("cell 2:")
	#print(cells[0])
	


	for i in range(len(prev_start_points)):
		test1 = current_cell == cells[i]
		test1=test1.all()
		if test1 == True:
			#print("test2")
			test2 = current_positions == positions[i]
			test2=test2.all()
			if test2 == True:
				#print("test3")
				test3 = current_species == species[i]
				test3=test3.all()
		
		if test1 == True:
			if test2 == True:
				if test3 == True:
					check=True
					#print(str("function "+str(check)),end="\n\n" )
					return check
					
	if check == None:
		check = False
	
	return check
	
	
#write function to compare current proposed structure to all previous structures
#then need to add into "run_fuse.py" to write all previous structures as a pickle file
#so that we can recover the start points between runs
