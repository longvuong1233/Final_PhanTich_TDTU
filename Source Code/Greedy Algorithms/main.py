# Nội dung:
#  code python 3 thuật toán cơ bản về Greedy gồm Prim, Kruskal và Dijkstra


# ----------------------


# thuật toán Prim


# ----------------------

from collections import defaultdict


def prim(graph):
    key = [float("inf")] * len(graph[0])
    parent = [None] * len(graph[0])

    key[0] = 0
    mstSet = [False] * len(graph[0])

    parent[0] = -1

    for i in range(len(graph[0])):
        u = minKey(key, mstSet, len(graph[0]))
        mstSet[u] = True
        for v in range(len(graph[0])):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    result = []
    for i in range(1, len(graph[0])):
        result.append(repr(parent[i]) + "-" + repr(i))
    return result


def minKey(key, mstSet, v):

    min = float("inf")

    for v in range(v):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return min_index


# --------------------------

# Thuật toán Kruskal

def kruskal(Graph):

    result = []

    i = 0

    e = 0

    Graph.graph = sorted(Graph.graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(Graph.V):
        parent.append(node)
        rank.append(0)

    while e < Graph.V - 1:
        u, v, w = Graph.graph[i]
        i = i + 1
        x = Graph.find(parent, u)
        y = Graph.find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            Graph.union(parent, rank, x, y)

    minimumCost = 0
    minPath = []
    for u, v, weight in result:
        minimumCost += weight
        minPath.append(repr(u)+"-"+repr(v))
    return minPath


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1


# ----------------------------------

# Thuật toán dijkstras

def dijkstra(graph, src):

    dist = [float('inf')] * len(graph[0])
    dist[src] = 0
    sptSet = [False] * len(graph[0])

    for count in range(len(graph[0])):

        u = minDistance(len(graph[0]), dist, sptSet)

        sptSet[u] = True

        for v in range(len(graph[0])):
            if graph[u][v] > 0 and \
                    sptSet[v] == False and \
                    dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


def minDistance(V, dist, sptSet):
    min = float("inf")

    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index
