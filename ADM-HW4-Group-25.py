
############################### Part - 1 ###################################
''' Here we use DBLP dataset, we are given two json files. full_DBLP (which contains
the whole network) and reduced_DBLP(which is a reduced version of the full_DBLP)
In the first part, we process the json and parse it. We create a graph G, whose 
nodes are authors. The nodes are connected if the authors have a common publication
And the weight of the edges are calculated by Jaccard Similarity.
'''
import json
import matplotlib.pyplot as plt
#from pprint import pprint
# Loading the json file
data = json.load(open('/Users/venkatapochiraju/Downloads/ADM4/reduced_dblp.json')) 
# We have written all the functions that we used in modules.py
# so, let's import that file as mo
import modules as mo

publications = {} # we will load all the publications into this dictionary
for i in range(len(data)):
    lst = []
    for j in data[i]['authors']:
        lst.append(j['author_id'])
    # This dictionary will have author_id and their publications
    publications[data[i]['id_publication_int']] = lst 

from collections import defaultdict
# Making authors as a defaultdict for easy access
authors = defaultdict(list) 

for key, values in publications.items():
    for value in values:
        authors[value].append(key)

import itertools
import networkx as nx
# Creating an empty graph
graph = nx.Graph()

for pub, aut in publications.items():
    if len(aut)>1:
        # we need all the combinations, so we use combinations function from 
        # itertools package
        combos = list(itertools.combinations(aut,2))
        for names in combos:
            # Adding edges
            graph.add_edge(names[0], names[1], weight = mo.jaccard_distance(authors[names[0]], authors[names[1]]))
    else:
        graph.add_node(aut[0])
# To print the information about the graph like:
# Type, number of nodes, edges and the average degree
print(nx.info(graph))
# Plotting the whole graph
mo.plot_graph(graph)

############################### Part - 2 ####################################
'''
In the second part, we compute statistics and visualize them. 
'''
############################### Part - 2a ###################################
'''
given a conference in input, we plot the subgraph induced by the set of authors who
published at that conference. And also compute some centralities measures like
degree, closeness, betweeness and plot their histograms
'''
conference=input("Enter the conference_id:")
data[0] # Just to check the data
graph.nodes(data=True)

authors_list=[]
c=int(conference)
# Finding all the authors that have published at the given input conference
for instance in data:
    current_c=int(instance['id_conference_int'])
    if current_c == c:
        for a in instance['authors']:
            if a['author_id'] not in authors_list:
                authors_list.append(a['author_id'])
    
print(authors_list)
# Inducing a subgraph from the whole graph with the authors published in the
# input conference as nodes
H = graph.subgraph(authors_list)
# To print the information about the graph like:
# Type, number of nodes, edges and the average degree
print(nx.info(H))
# Plotting the subgraph
mo.plot_graph(H)

list_names={}
for instance in data:
    for a in instance['authors']:
        if int(conference)==int(instance['id_conference_int']):
            
            times=list_names.get(a['author'], 0)
            times+=1
            if times !=0:
                list_names[a['author']]=times
            else:
                continue      
plt.figure()
plt.hist(list(list_names.values()))
plt.show()

# DEGREE CENTRALITY
degree_centrality={}
n=len(H)
for each in H:
    degree_centrality[each]=len(H.edges(each))/(n-1)
print(degree_centrality)

 ### TRY TO PLOT HIST OF DEGREE CENTRALITY FOR GRAPH ###

degree_sequence=sorted(nx.degree(graph).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)

plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")
# draw graph in inset
plt.axes([0.45,0.45,0.45,0.45])
Gcc=sorted(nx.connected_component_subgraphs(graph), key = len, reverse=True)[0]
pos=nx.spring_layout(Gcc)
plt.axis('off')
nx.draw_networkx_nodes(Gcc,pos,node_size=20)
nx.draw_networkx_edges(Gcc,pos,alpha=0.4)
plt.savefig("degree_histogram.png")
plt.show()
##data rate exceed for full_data

# For the induced subgraph - H
degree_sequence=sorted(nx.degree(H).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)
plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")
# draw graph in inset
plt.axes([0.45,0.45,0.45,0.45])
Gcc=sorted(nx.connected_component_subgraphs(H), key = len, reverse=True)[0]
pos=nx.spring_layout(Gcc)
plt.axis('off')
nx.draw_networkx_nodes(Gcc,pos,node_size=20)
nx.draw_networkx_edges(Gcc,pos,alpha=0.4)
plt.savefig("degree_histogram_H.png")
plt.show()

# Histogram for degree centrality
centralityValues = []
for key in degree_centrality.keys():
    centralityValues.append(degree_centrality[key])
print('Degree Centrlality histogram')
plt.ylabel('Frequency')
plt.hist(centralityValues)
plt.show()

#ABSOLUTE CENTRALITY
centrality={}
s=1.0/(len(graph)-1.0)
centrality=dict((n,d*s) for n,d in H.degree_iter())
#plt.hist(centrality)
centrality

centralityValues = []
for key in centrality.keys():
    centralityValues.append(centrality[key])
print('Absolute Centrlality histogram')
plt.ylabel('Frequency')
plt.hist(centralityValues)
plt.show()

# BETWEENNESS CENTRALITY
betweeness_centrality={}
n=len(H)
denom=n**2 - 3*n + 2
for id_author in centrality.keys():    
    betweeness_centrality[id_author]=centrality[id_author]/denom
betweeness_centrality

betweenessValues = []
for key in betweeness_centrality.keys():
    betweenessValues.append(betweeness_centrality[key])
print('Betweenness Centrality histogram')
plt.ylabel('Frequency')
plt.hist(betweenessValues)
plt.show()

############################### Part - 2b ###################################
'''
given an author and an integer d as input, we plot the subgraph induced by the nodes 
that have hop distance (i.e., number of edges) at most equal to d with the input author.
And we visualize the graph.
'''
authorInp = input("Enter the author id :")
d = int(input("Enter d: "))
subGraph = nx.ego_graph(graph, int(authorInp), radius = d)
#nx.draw(subGraph, pos=nx.spring_layout(subGraph),with_labels = True)
print(nx.info(subGraph))
mo.plot_graph(subGraph)

############################### Part - 3 ####################################
'''
In the third part, we will compute a generalized version of the Erd¨os number
'''

############################### Part - 3a ###################################
'''
Given an author_id as input, we wrote a function dijkstra which returns the
weight of the shortest path that connects the input author with Aris. 
'''
authorIdInp = int(input("Enter author_id:"))
weight = mo.dijkstra(graph, 256176, authorIdInp)
print("The weight of the shortest path that connects "+ authorIdInp + "with Aris is: " + weight)
############################### Part - 3b ###################################
'''
Given a subset of nodes (Cardinality smaller than 21), we wrote a function dijkstra2
which returns, for each node of the graph, its Group Number
'''
subsetInp = list(map(int,input("Enter a subset of nodes (Cardinality smaller than 21) separated by spaces: ").split()))
all_distances = mo.dijkstra2(graph, subsetInp)
#all_distances = mo.dijkstra2(graph, [256176, 273893, 44955, 256177, 523303])
all_distances # This is a dictionary, where keys are the authors and their values are group numbers
for key in all_distances.keys():
    print("The Group number of the node '" + str(key) + "' is : " + str(all_distances[key]))

















