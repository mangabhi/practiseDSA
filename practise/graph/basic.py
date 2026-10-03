from collections import deque

class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,node,neighbours):
        self.graph[node]=neighbours

    def bfs(self,start):
        visited={start}
        q=deque([start])
        while q:
            node = q.popleft()
            print(node,end=" ")
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)

    def dfs(self,node,visited=None):
        if visited is None:
            visited=set()
        visited.add(node)
        print(node,end=" ")
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs(neighbour,visited)

    def find_center(self,edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
    
    def valid_path(self,n,edges,source,destination):

        #create adjancey matrix
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited={source}
        q=deque([source])
        while q:
            curr=q.popleft()
            if curr == destination:
                return True
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
        return False 

    def number_of_province(self,isConnected):
        n=len(isConnected)
        visited=set()
        provinces=0

        def dfs(city):
            visited.add(city)

            for neighbour in range(n):
                if isConnected[city][neighbour] ==1:
                    if neighbour not in visited:
                        dfs(neighbour)

        for city in range(n):
            if city not in visited:
                provinces +=1
                dfs(city)

        return provinces

    def adjancey_list(self,numCourses:int,prerequisites)-> bool:
        graph={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            graph[crs].append(pre)
        
        visited=set()

        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):return False
            visited.remove(course)
            graph[course]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs) : return False
        return True




g=Graph()
g.add_edge("A",["B","C"])
g.add_edge("B",["D","E"])
g.add_edge("C",["F"])
g.add_edge("D",[])
g.add_edge("E",[])
g.add_edge("F",[])
edges = [[1, 2], [2, 3], [4, 2], [2, 5]]
# g.bfs("A")
# g.dfs("A")
# print(g.find_center(edges))
n = 3
edges = [[0,1], [1,2]]
source = 0
destination = 3

print(g.valid_path(n,edges,source,destination))