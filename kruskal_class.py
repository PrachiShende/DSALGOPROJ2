class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, x, y, z):
        self.graph.append([x, y, z])
    def find(self, parent, i):
        if i > len(parent):
            i = parent[len(parent)-1]
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        x_source = self.find(parent, x)
        y_source = self.find(parent, y)
        if rank[x_source] < rank[y_source]:
            parent[x_source] = y_source
        elif rank[x_source] > rank[y_source]:
            parent[y_source] = x_source
        else:
            parent[y_source] = x_source
            rank[x_source] += 1
    def KruskalMinSpanTree(self):
        result = []
        edge = i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        position = []
        for node in range(self.V):
            parent.append(node)
            position.append(0)
        while edge < self.V - 1:
            if i >= len(self.graph):
                break
            start, finish, weight = self.graph[i]
            i += 1
            x = self.find(parent, start)
            y = self.find(parent, finish)
            if x != y:
                edge = edge + 1
                result.append([start, finish, weight])
                self.union(parent, position, x, y)
        print("Edge Selected \t Weight" )
        res=0
        for start, finish, weight in result:
            print("   ",chr(start + 65), "->", chr(finish + 65), '       ', weight)
            res+=weight
        print("The total Cost for Minimum Spanning Tree is", res)
        
