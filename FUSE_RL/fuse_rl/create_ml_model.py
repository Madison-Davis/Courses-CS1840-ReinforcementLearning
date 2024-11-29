import numpy
import pandas
import sklearn
from ase.visualize import *
import pickle

def create_ml_model(ini_structures='',search_structures=''):
	#first need to assemble all of the structuers into a pandas dataframe
	strings=[]
	instructions=[]
	energies=[]
	keys=list(ini_structures.keys())
	for i in range(len(keys)):
		strings.append(ini_structures[keys[i]][1])
		instructions.append(ini_structures[keys[i]][2][1:])
		energies.append(ini_structures[keys[i]][3])
	
	keys=list(search_structures.keys())
	del keys[0]
	
	for i in range(len(keys)):
		strings.append(search_structures[keys[i]][1])
		instructions.append(search_structures[keys[i]][2][1:])
		energies.append(search_structures[keys[i]][3])
			
	data={'strings':strings,'instructions':instructions,'energies':energies}
	data=pandas.DataFrame(data)
	pickle.dump(data,open("data.p",'wb'))
	sys.exit()
