ADM HW-4 Group – 25

Alessandra Griesi, Malik Bekmurat, Venakta Naga Sai Krishna Abhinay Pochiraju

https://github.com/pvnskabhinay/ADM-HW4-Group-25

The purpose of this homework is to extract information from the given json files. we are given two json files. full_DBLP (which contains the whole network) and reduced_DBLP(which is a reduced version of the full_DBLP). In the first part, we process the json and parse it. We create a graph G, whose nodes are authors. The nodes are connected if the authors have a common publication, and, the weight of the edges are calculated by Jaccard Similarity. Then, the second part is computing some statistics and visualizing them. And finally the third part is computing generalized version of the Erdös number.

JSON’S Scheme:

The json files given are organized in the following format:
-	authors: it is a list of dictionaries, with keys author (name of the author) and author_id
-	id_conference: the conference id
-	id_conference_int: the numerical conference id
-	id_publication: the publication id
-	id_publication_int: the numerical publication id
-	title: the title of the publication

Installing required packages/modules:
We need to install and import the following modules:
-	matplotlib
-	networkx
-	heapq
-	json
-	itertools

modules.py:

This file contains all the methods/functions that we defined and are going to use in the main task. The functions are as follows: 
-	jaccard_distance(list1, list2)
This function is used to calculate the jaccard distance between the two input arguments and then calculate the weight of the edge between two nodes using w = 1-J(p1,p2)
-	plot_graph(graph)
This function is defined to visualize the input argument, which is a graph
-	dijkstra(graph, source, destination)
Function for finding weight of the shortest path from a source node to any given node in the graph
-	dijkstra2(graph, sub_gr)
Function for finding weight of the shortest path from closest node in sub group to each node in graph
These functions are explained below. And also, we have to import modules to access these functions in the main code.
The main TASK:

Part-1: We parsed the data from the given json files, and organized them into a dictionary (publications - composed by publication_id (key) and list of author_ids (values)) and used this dictionary to add nodes for the graph. So, for each key – value of publications, we add a node with label author_id. When the list in value is more than 1, we connect the nodes using the function add_edge(). To find the weight of this edge, we used an user-defined function jaccard_distance(), which determines the weight for each edge connecting the authors that are passed as arguments. Once we calculate the Jaccard distance for 2 nodes, the weight of the edge connecting those two nodes is equal to (1-Jaccard_distance). After all the edges have been added, to visualize the graph, we defined another function plot_graph() , which uses draw_networkx_nodes(),draw_networkx_edges(), and show() functions to show the graph. 

Part-2a: Given a conference id, we created a list of all the authors that presented at that conference, and induced a subgraph with the authors list that we created as nodes using the inbuilt function subgraph(). Again we visualized it with plot_graph() method. We calculated degree, betweeness and closeness centralities by following the formulae on Graph’s notes, and also visualized them using histograms. 

Part-2b: Given an input node and an integer d, to visualize the subgraph induced by the nodes that have hop distance at most equal to d with the input author, we used an inbuilt function ego_graph() which returns the induced subgraph of neighbours centred at node n within a given radius. And then again used the function plot_graph() to visualize it. 

Part-3: Generalized version of the Erdös number. We defined two functions: 
-	dijkstra(graph, source, destination)
-	dijkstra2(graph, sub_gr)

In the first one, we heap queue to implement the algorithm. We have two lists of nodes. One takes trace of the visited nodes, and the other is used to take the minimum total weight from the target/destination node. At the end, it returns the shortest distance from the input author to Aris. 

The second dijkstra also uses the same trick with heap. We pop from heap the minimum weight related to the node and check with the dictionary’s weight. If it is less, we update the dictionary with the new node. Meanwhile, we add the node to visited list, and add to heap (named prelim), the minimum distances calculated.

