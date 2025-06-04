from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.graph=defaultdict(set)
        self.reverse_graph=defaultdict(set)
        self.num=n
    def add_edge(self, a, b):
        self.graph[a].add(b)
        self.reverse_graph[b].add(a)
    def topological_order(self) -> bool:
        q=deque()
        stack=[]
        for i in range(self.num):
            if len(self.reverse_graph[i])==0:
                q.append(i)
        while q:
            cur=q.popleft()
            stack.append(cur)
            for i in list(self.graph[cur]):
                self.reverse_graph[i].remove(cur)
                if self.reverse_graph[i]==set():
                    q.append(i)
        if len(stack)==self.num:
            return True
        else:
            return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=Graph(numCourses)
        for i in prerequisites:
            graph.add_edge(i[1], i[0])
        return graph.topological_order()

