import time
import math
from Dijkshitra_class import Dijkstra
from kruskal_class import Kruskal
from SCC_Class import SCC_class,StrongConnectedComponents
import sys

def dijkstra():
    print("------------------Shortest Path Dijkstra Algorithm-------------------")
    directed=False
    for count in range(9):
        f1 = open("input"+str(count)+".txt","r")
        i=0
        print("\n Shortest path for the Graph", str(count), "\n")
        for line in f1.readlines():
            line_array = line.split()
            if i == 0:
                print('Number of Vertices: ', int(line_array[0]))
                print('Number of Edges: ', int(line_array[1]))
                if line_array[2] == "U":
                    print("The Graph is UNDIRECTED ")
                    directed = False
                else:
                    print("The Graph is DIRECTED ")
                    directed = True
                graph = Dijkstra(directed)
            elif len(line_array) == 1:
                src = ord(line_array[0])-65
            else:
                graph.addEdge(ord(line_array[0])-65,ord(line_array[1])-65,int(line_array[2]))
            i = i + 1
        print("Source vertex:",chr(src+65))
        print()
        begin_time = time.time()
        parent, distance = graph.dijkstra(src)
        graph.printShortestpath(distance, parent, src)
        runtime = (time.time() - begin_time) * 1000
        print()
        print('Runtime for Dijkstras Algorithm:',math.ceil(runtime)," Seconds")
        print('\t')

def kruskal():
    print("-------------------Minimum Spanning Tree (Kruskal Algorithm)-------------------\t")
    for count in range(5,9):
        print("Minimum Spanning Tree for graph", str(count))
        f1 = open("input" + str(count) + ".txt", "r")
        i = 0
        for line in f1.readlines():
            line_array = line.split()
            if i == 0:
                graph = Kruskal(int(line_array[0]))
            elif len(line_array) == 1:
                pass
            else:
                graph.addEdge(ord(line_array[0]) - 65, ord(line_array[1]) - 65, int(line_array[2]))
            i = i + 1
        begin_time = time.time()
        graph.KruskalMinSpanTree()
        runtime = (time.time() - begin_time) * 1000
        print()
        print('Runtime for Kruskal Algorithm:', math.ceil(runtime),"Seconds")
        print('\t')

def stronglyconnectedcomponents(): 
    print("------------------Strongly Connected Components-------------------\t\t")
    strongly_connected_components = StrongConnectedComponents()
    for count in range(9):
        print("Strongly connected components for graph" + str(count))
        f1 = open("input" + str(count) + ".txt", "r")
        edges = []
        i = 0
        for line in f1.readlines():
            x = line.split()
            if i == 0:
                number_of_vertices = int(x[0])
                print("No.of vertices: ", number_of_vertices)
            elif len(x) == 1:
                pass
            else:
                edges.append((ord(x[0]) - 65, ord(x[1]) - 65))
            i = i + 1
        begin_time = time.time()
        result = strongly_connected_components(SCC_class(edges))
        for j in range(len(result)):
            for k in result[j]:
                print(k,end=" ")
        runtime = (time.time() - begin_time) * 1000
        print('\n Runtime for calculating SCC:', math.ceil(runtime),"Seconds")
        print('\t')

dijkstra()
kruskal()
stronglyconnectedcomponents()
