from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.graph=defaultdict(set)
        self.reverse_graph=defaultdict(set)
        self.num=n
    def add_edge(self, a, b):
        self.graph[a].add(b)
        self.reverse_graph[b].add(a)
    def topological_order(self):
        q=deque()
        stack=[]
        for i in range(self.num):
            if len(self.reverse_graph[i])==0:
                q.append((i, 0))
        while q:
            cur, layer=q.popleft()
            stack.append((cur, layer))
            for i in list(self.graph[cur]):
                self.reverse_graph[i].remove(cur)
                if self.reverse_graph[i]==set():
                    q.append((i, layer+1))
        return stack

n, m=map(int, input().split())
graph=Graph(n)
for i in range(m):
    a, b=map(int, input().split())
    graph.add_edge(b, a)

stack=graph.topological_order()
ans=n*100
for i in stack:
    ans+=i[1]
print(ans)
