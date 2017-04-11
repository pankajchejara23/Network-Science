############################################################
#
#  Random Network Generation
#  Developer : Pankaj Chejara
#              PhD Scholar
#              ABV-IIITM, Gwalior
#
############################################################

import networkx as nx
import matplotlib.pyplot as plt
import random as r

def generate_random(N,p):
	for i in range(N):
		for j in range(N):
			if(i!=j and i < j):
				if(r.random()<p):
					f.write("%s %s\n" %(i,j))

					

f=open("data.txt",mode='w')
generate_random(100,.3)
f.close()

g=nx.read_edgelist("data.txt",create_using=nx.Graph())
nx.write_gml(g,"data.gml")
print(nx.info(g))			
