from collections import deque
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = deque([vertex])
        print("\nBFS :",end=" ")
        while queue:          # Time complexity : O(V+e)   space complexity:O(v)
            deVertex = queue.popleft()
            print(deVertex,end=" ")
            for adjacentVertex in self.gdict[deVertex]:         
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
                    
    def dfs(self,vertex):
        visited = set()
        print("\nDFS :",vertex,end=" ")
        visited.add(vertex)
        stack = [vertex]
        while stack:  # Time complexity : O(V+e)     space complexity:O(v)
            node = stack.pop()
            if node not in visited:
                print(node,end=" ")
                visited.add(node)
            for adj_vertices in self.gdict[node]:
                if adj_vertices not in visited:
                    stack.append(adj_vertices)

customDict = { "a" : ["b","c"],
              "b" : ["a","d","e"],
              "c" : ["a","e"],
              "d" : ["b","e","f"],
              "e" : ["d","f"],
              "f" : ["d","e"]
              }

graph = Graph(customDict)
graph.bfs("a")
graph.dfs("a")
#        a
#       / \
#      b   c
#      | \ |
#      d-- e
#       \  /
#         f
#
#