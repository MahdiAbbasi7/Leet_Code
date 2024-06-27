'''
Python3 program to print a DFS traversal 
from a given source vertex. DFS(int s)
traverses vertices reachable from s.
'''

from collections import defaultdict

class Graph:
    '''This class represents a directed graph using adjacency list representation.'''
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        '''A function used by DFS. mark the current node as visited and print.'''
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
        
    def DFS(self, v):
        '''The function to do DFS traversal. It uses recursive DFSUtil()'''
        visited = [False] * (max(self.graph)+1)

        self.DFSUtil(v, visited)


g = Graph()
g.add_Edge(0, 1)
g.add_Edge(0, 2)
g.add_Edge(1, 2)
g.add_Edge(2, 0)
g.add_Edge(2, 3)
g.add_Edge(3, 3)

print("Following is Breadth First Traversal")
g.DFS(2) # 2 0 1 3