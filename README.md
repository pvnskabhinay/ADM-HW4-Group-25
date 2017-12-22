# ADM-HW4-Group-25
                                                    Homework 4 – Group 25
The purpose of this homework is to extract informations of files json about conferences linked by authors that have publications in common.	This, in order to create graphs and make statistics to show up graphically the informations synthesized.  
We started to examinate the json’s files in order to understand how to make graph, detecting how all informations were linked togheter and the we have created the function asked.
All functions and Jupyter block are already runned and we can see plots already if we open files on github.
But we can find also plots into report.

JSON ‘S Scheme
It is organized in this way:
-List of authors, with names and ids respective.
-Id of conference
-Id conference with int format
-Id publication
-Id publication in int format
-Title of conference
So, each instance was composed by these values.

Installing
We needed to install  and import modules like matplotlib.pyplot and networkx

Running the tests

As we already said, all modules (cells) are already runned.
So, starting from point 1:
We had to organize the json into dictionary  (publications dict composed by publication id as key and list of authors ids as value) and use it for creating the graph’s node.
So, for each key – value of publications, we take author_id and make nodes.
When the list in value is more than 1, we make link using add_edge.
Jaccard_distance is the function that determs  the weight for each edge, putted in add_edge function.
Once created the graph, we make a plot using draw_networkx_nodes.

For the second part, the task was first to find , given a conference id, the authors that have published for that conference. And to make some statistics.
So we created a list of author that contains all of them. We created a graph of this list and calculate degreeness, betweeness and closeness centrality and plot all of them.
We followed the formulas on Graph’s notes for compute all centralities.
For the b) point of second part, we used ego_graph function to take all nodes with at most d distance hop. A node was entered in input and we compute for that node.
And then, plot it using again draw_networkx.

For the third part we make two functions: the first calculated the shortest path from a node (author_id) to Aris, with the minimum weight. And it returns the weight.

Signature of method: dijkstra(graph, source, destination)

Heap queue used for implement the algorithm. We have two lists of nodes.
One take trace of visited nodes, and the other is used to take the less total weight from our target/destination node.
At the end, it returns distance taked from (distance, node=’Aris’) 
The part b) of hird point asks, taken a set of 21 nodes, all the shortest paths that linked to the other nodes. We made this only with 5 nodes, for computational problems. Also this method uses heap queue.

Signature of method: dijkstra2(graph, sub_gr)	

The second dijkstra use the same trick with heap: we pop from heap the minimum weight related to the node  and check with the dictionary’s weight. If it is less, we update the dictionary with the new node.
Meanwhile, we add the node to visited list, and add to heap (named prelim ) the minimum distances calculated.  

