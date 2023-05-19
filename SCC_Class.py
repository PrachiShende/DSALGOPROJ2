from itertools import chain
from collections import defaultdict

class SCC_class(object):
    def __init__(self, edges, vertices=()):
        self.edges = edges
        self.vertices = set(chain(*edges)).union(vertices)
        self.tails = defaultdict(list)
        for head, tail in self.edges:
            self.tails[head].append(tail)

    def from_dict(cls, edge_dict):
        return cls((k, v) for k, vs in edge_dict.items() for v in vs)

class StrongConnectedComponents(object):
    def strong_connect(self, head):
        low, count, stack = self.low, self.count, self.stack
        low[head] = count[head] = self.counter = self.counter + 1
        stack.append(head)
        for tail in self.graph.tails[head]:
            if tail not in count:
                self.strong_connect(tail)
                low[head] = min(low[head], low[tail])
            elif count[tail] < count[head]:
                if tail in self.stack:
                    low[head] = min(low[head], count[tail])
        if low[head] == count[head]:
            component = []
            while stack and count[stack[-1]] >= count[head]:
                component.append(chr(stack.pop()+65))
            self.connected_components.append(component)

    def __call__(self, graph):
        self.graph = graph
        self.counter = 0
        self.count = dict()
        self.low = dict()
        self.stack = []
        self.connected_components = []
        for v in self.graph.vertices:
            if v not in self.count:
                self.strong_connect(v)
        return self.connected_components
