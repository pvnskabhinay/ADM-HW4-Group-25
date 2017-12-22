#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:09:12 2017

@author: venkatapochiraju
"""
import networkx as nx

def jaccard_distance(list1, list2):
    # The function to calculate the weights
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    if int(union)==0:
        return 0
    return 1-float(intersection / union)

def plot_graph(graph):
    from pylab import show
    # create the layout
    pos = nx.random_layout(graph)
    # draw the nodes and the edges (all)
    nx.draw_networkx_nodes(graph,pos,node_color='b',alpha=0.2,node_size=8)
    nx.draw_networkx_edges(graph,pos,alpha=0.1)
    
    # draw the most important nodes with a different style
    #nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
    # also the labels this time
    #nx.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
    show()
    
import heapq
def dijkstra(graph, source, destination):
    
    """Function for finding weight of the shortest path 
    from a source node to any given node in the graph"""
    
    #prelim is a list with nodes that have been reached but its neigbors were not investigated
    #visited is a set of nodes whose neigbors were investigated
    prelim = [(0, source)]
    visited = set()
    #loop which stops when destination node is achieved and its distance to the source is calculated
    while destination not in visited:
        #heap is used in order to keep list of nodes in a structured manner
        #so that dijkstra's algorithm worked in a fast manner
        (distance, node) = heapq.heappop(prelim)
        #if the node is in visited set then it is fully investigated
        #and only if it is not in the set then operations take place
        if node not in visited:
            visited.add(node)
            #each node neighbouring with the node with minimam distance (from pop)
            #is investigated and distances for each of them are calculated
            #and results are saved in prelim list
            for (edge, dist) in graph[node].items():
                heapq.heappush(prelim, (distance + dist['weight'], edge))
    return distance


#import heapq
def dijkstra2(graph, sub_gr):
    
    """Function for finding weight of the shortest path 
    from closest node in sub group to each node in graph"""
    
    #dictionary of a GroupNumber(v) = min{ShortestPath(v,u)} for each node in a graph
    all_dist = {}
    
    #loop which iterates through each node in a given sub group
    #and finds distance to each node in the graph
    for part in sub_gr:
        
        #prelim is a list with nodes that have been reached but its neigbors were not investigated
        #visited is a set of nodes whose neigbors were investigated
        prelim = [(0, part)]
        visited = set()
        
        #loop which is run to check each node's distance 
        #to the given node in the graph subgraph
        while prelim:
            
            #heap is used in order to keep list of nodes in a structured manner
            #so that dijkstra's algorithm worked in a fast manner
            (distance, node) = heapq.heappop(prelim)
            
            #if the node from graph was not added to the all_dist dictionary
            #or if the new distance is shorter
            #node and its distance is added to the dictionary
            if node not in all_dist or all_dist[node] > distance:
                all_dist[node] = distance
            
            #if the node is in visited set then it is fully investigated
            #and only if it is not in the set then operations take place
            if node not in visited:
                visited.add(node)
                
                #each node neighbouring with the node with minimam distance (from pop)
                #is investigated and distances for each of them are calculated
                #and results are saved in prelim list
                for (edge, dist) in graph[node].items():
                    heapq.heappush(prelim, (distance + dist['weight'], edge))
    return all_dist