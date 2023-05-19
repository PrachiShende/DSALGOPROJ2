from collections import defaultdict
import math
import sys
class Dijkstra:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    def addEdge(self, begin, end, weight):
        self.graph[begin].append([end, weight])
        if self.directed is False:
            self.graph[end].append([begin, weight])
        elif self.directed is True:
            self.graph[end] = self.graph[end]
    def get_min(self, distance, visited):
        min = float('inf')
        index = -1
        for i in self.graph.keys():
            if visited[i] is False and distance[i] < min:
                min = distance[i]
                index = i
        return index
    def dijkstra(self, src):
        visited = {i: False for i in self.graph}
        distance = {i: float('inf') for i in self.graph}
        parent = {i: None for i in self.graph}
        distance[src] = 0
        for i in range(len(self.graph) - 1):
            x = self.get_min(distance, visited)
            visited[x] = True
            for v, w in self.graph[x]:
                if visited[v] is False and distance[x] + w < distance[v]:
                    distance[v] = distance[x] + w
                    parent[v] = x
        return parent, distance
    def printPath(self, parent, v):
        if parent[v] is None:
            return
        self.printPath(parent, parent[v])
        print(chr(v+65),end=" ")
    def printShortestpath(self, distance, parent, src):
        for i in self.graph.keys():
            if i == src:
                continue
            if i < 0:
                break
            if distance[i]==float("inf"):
                continue
            print('Cost of shortest path from the node {} -> {} is \t{} and path is \t{}'.format(chr(src+65), chr(i+65), distance[i], chr(src+65)), end=' ')
            self.printPath(parent, i)
            print()

