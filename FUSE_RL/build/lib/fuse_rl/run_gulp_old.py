import sys
import os
import glob
from ase import *
from fuse_rl.gulp import *
from ase.calculators.gulp import GULP
import platform
import re
from ase.io import *
#target = "temp01.res"
#restart= "restart.res"
#head = "head2.txt"

def run_gulp(atoms='',shel=None,kwds='',opts='',lib='',produce_steps=''):
	iat=len(atoms)
	converged = False
	if os.path.isfile("temp.res"):
		os.remove("temp.res")
	if produce_steps==True:
		try:
			files=glob.glob("atoms*.cif")
			for z in range(len(files)):
				os.remove(files[z])
		except:
			pass
	for i in range(len(kwds)):
		#print(i+1)
		#atoms.rattle(0.01)
		if not 'dump temp.res\n' in opts[i]:
			opts[i].append('dump temp.res\n')
		if shel == None:
			calc=GULP(keywords=kwds[i],options=opts[i],library=lib)
		else:
			calc=GULP(keywords=kwds[i],options=opts[i],library=lib,shel=shel)
		atoms.set_calculator(calc)
		atoms.get_calculator().optimized = False
		try:
			energy=atoms.get_potential_energy()
			if len(atoms) != iat:
				converged = False
				break
			try:
				if glob.glob("gulptmp*") != []:
					if platform.system() == 'Windows':
						files=glob.glob("gulptmp*")
						for z in range(len(files)):
							os.remove(files[z])
					if platform.system() == 'Linux':
						os.system("rm gulptmp*")
			except:
				pass
		except:
			f=open("gulp.gin",'r')
			f2=f.readlines()
			cell=re.findall("\d+\.\d+",f2[6])
			for i in range(len(cell)):
				cell[i]=cell[i][:10]
				
			f.close()
			f3=open("gulp.gin",'w')
			f2[6]=str(str(cell[0])+" "+str(cell[1])+" "+str(cell[2])+" "+str(cell[3])+" "+str(cell[4])+" "+str(cell[5])+"\n")
			for i in range(len(f2)):
				f3.write(f2[i])
			f3.close()
			atoms=read_gulp("gulp.gin")
			atoms.set_calculator(calc)
			try:
				energy=atoms.get_potential_energy()
				if len(atoms) != iat:
					converged = False
					break
				if glob.glob("gulptmp*") != []:
					if platform.system() == 'Windows':
						os.system("del gulptmp*")
					if platform.system() == 'Linux':
						os.system("rm gulptmp*")
			except:
			#except(ValueError):
				energy=1.0e20
			#	break
		if atoms.get_calculator().optimized == True:
			if atoms.calc.Gnorm <= 0.01:
				#converged = True
				#try:
				#	atoms = read_gulp("temp.res")
				#except:
				#	converged = False
				#	pass
				
				### add in extra check to see if the calculation has REALLY converged
				f4=open("gulp.got",'r').readlines()
				if 'opti' in kwds[i]:
					if not '  **** Optimisation achieved ****' in f4:
						converged = True
					else:
						converged = False
		
		if 'sing' in kwds[i]:
			converged = True

		if produce_steps==True:
			label=str("atoms"+str(i+1)+".cif")
			write(label,atoms)
		#os.remove("gulp.got")
		#os.remove("gulp.gin")
		try:
			atoms = read_gulp("temp.res")
		except:
			pass
	if converged == True:
		try:
			atoms = read_gulp("temp.res")
		except:
			pass
	else:
		converged = False
		energy = 1.0e20
		
	#view(atoms)
	return atoms, energy, converged

