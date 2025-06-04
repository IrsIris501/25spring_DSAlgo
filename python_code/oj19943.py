class Vertex:
    def __init__(self, key):
        self.id=key
        self.neighbor=set()

class Graph:
    def __init__(self, n):
        self.vert_dict=dict()
        for i in range(n):
            self.vert_dict[i]=Vertex(i)
    def add_edge(self, a, b):
        self.vert_dict[a].neighbor.add(self.vert_dict[b])
        self.vert_dict[b].neighbor.add(self.vert_dict[a])

n, m=map(int, input().split())
graph=Graph(n)
for _ in range(m):
    a, b=map(int, input().split())
    graph.add_edge(a, b)

d=[[0 for i in range(n)] for j in range(n)]
a=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    d[i][i]=len(graph.vert_dict[i].neighbor)
for i in range(n):
    for j in range(i+1, n):
        if graph.vert_dict[i] in graph.vert_dict[j].neighbor:
            a[i][j]=1
            a[j][i]=1

l=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        l[i][j]=d[i][j]-a[i][j]
for i in range(n):
    print(*l[i])
