'''
Python3 program to print a BFS traversal 
from a given source vertex. BFS(int s)
traverses vertices reachable from s.
'''

from collections import defaultdict

class Graph:
    '''This class represents a directed graph using adjacency list representation.'''
    def __init__(self) -> None:
        self.graph = defaultdict(list)


    def add_Edge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        visited = [False] * (len(self.graph)) #[False, False, ...]

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end= ' ')
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



g = Graph()
g.add_Edge(0, 1)
g.add_Edge(0, 2)
g.add_Edge(1, 2)
g.add_Edge(2, 0)
g.add_Edge(2, 3)
g.add_Edge(3, 3)

print("Following is Breadth First Traversal")
g.BFS(2)