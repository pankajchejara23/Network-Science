############################################################
#
#  Erdős and Rényi Random Graph Generation
#  Developer : Pankaj Chejara
#              PhD Scholar
#              ABV-IIITM, Gwalior
#
############################################################

import networkx as nx
import matplotlib.pyplot as plt
import random as r


NUM_NODES=15
def generate_random(N,p):
	edge_list=[]
	if (p<0):
		print ("Probablity can't be negative")
		return
	if(p>1):
		print("Probablity can't be greater than 1")
		return
	for i in list((n,m) for n in range(N) for m in range(N)):
				if(r.random()<p):
					edge_list.append(i)
					
	return edge_list
					

l=generate_random(NUM_NODES,.1)
g=nx.Graph()
g.add_nodes_from(range(NUM_NODES))
g.add_edges_from(l)
print (g.nodes())

# Saving graph in gml format
nx.write_gml(g,"data-2.gml")
print(nx.info(g))			
