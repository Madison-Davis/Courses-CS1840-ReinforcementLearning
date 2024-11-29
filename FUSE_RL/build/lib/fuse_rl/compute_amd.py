from ase.io import *
import pandas
from ase import Atoms

def populate_nn_table(atoms1,atoms2,k):
	nn_table={} # nearest neighbour table, stored as dictionary while it's computed
	
	for i in range(k):
		nn_table[i+1]=[]
	
	for i in range(len(atoms1)):
		b_table=atoms2.get_distances(i,list(range(len(atoms2))),mic=True)
		b_table=sorted(b_table)
		if len(b_table) >= k:
			for j in range(k):
				nn_table[j+1].append(round(b_table[j],5))
		else:
			nn_table="fail"
			return nn_table
	return nn_table

def compute_amd(atoms1='',rep='',k=''):
	atoms2=atoms1.copy()
	atoms2=atoms2.repeat(rep)
	nn_table = "fail"
	
	while nn_table == "fail":
		nn_table=populate_nn_table(atoms1,atoms2,k)
		for i in range(len(rep)):
			rep[i]+=1
		atoms2=atoms1.copy()
		atoms2=atoms2.repeat(rep)
	
	data=pandas.DataFrame.from_dict(nn_table) # convert the nearest neighbour table to a DataFrame
	amd=list(data.mean())
	return amd


