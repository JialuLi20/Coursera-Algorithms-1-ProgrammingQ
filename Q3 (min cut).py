# This program finds the min cut by repeated randomized contraction algorithm #

import random, copy

# select a random edge (or two random vertices) from adjacency list #
def rEdge(adj_list) :
	vertex1 = adj_list.keys()[random.randint(0, len(adj_list)-1)]
	vertex2 = adj_list[vertex1][random.randint(0, len(adj_list[vertex1])-1)]
	return vertex1, vertex2
	
# define Krager's random contraction algorithm #
def minCut(adj_list):
	while len(adj_list) > 2 :
		vertex1, vertex2 = rEdge(adj_list)
		
		# add list of vertex2 to vertex1
		adj_list[vertex1].extend(adj_list[vertex2])
		
		# replace vertex2 with vertex in the adjacency list (contraction) #
		tmp_list = []
		for k in adj_list[vertex2]:
			tmp_list = adj_list[k]
			for i in range(0, len(tmp_list)) :
				if tmp_list[i] == vertex2 :
					tmp_list[i] = vertex1
			adj_list[k] = 	tmp_list	
		
		# remove self loop edges #
		while vertex1 in adj_list[vertex1] :
			adj_list[vertex1].remove(vertex1)
			
		# remove the whole list for vertex2 from the adjacency list #
		del adj_list[vertex2]
	
	return len(adj_list[adj_list.keys()[1]])

	
# read in file and make adjacency list #		
import os
direct= "file path"
fin= open(os.path.join(direct, "kargerMinCut.txt"), "r")   
adj_list = { }
for line in fin:	
	inputstr = []
	inputstr = line.split()
	x = inputstr.pop(0)
	adj_list[x] = inputstr	
	
	
# perform repeated random contraction algorithm #
min_cut_value =  minCut(copy.deepcopy(adj_list)) 
for i in range(1, 100) : 	
	x = minCut(copy.deepcopy(adj_list))	
	if x< min_cut_value :
		min_cut_value = x
		
print min_cut_value
	
	
	
	
	
