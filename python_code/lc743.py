import heapq
from collections import defaultdict
class Position:
    def __init__(self, destination, dist):
        self.destination=destination
        self.dist=dist
    def __gt__(self, other):
        return self.dist>other.dist

class Graph:
    def __init__(self, n):
        self.graph=defaultdict(set)
        self.num=n
    def add_edge(self, u, v, w):
        self.graph[u].add((v, w))

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=Graph(n)
        for u, v, w in times:
            graph.add_edge(u-1, v-1, w)
        visited=set()
        ans=0
        count=0
        heap=[Position(k-1, 0)]
        while heap and count<n:
            position=heapq.heappop(heap)
            dist=position.dist
            cur=position.destination
            if cur not in visited:
                visited.add(cur)
                count+=1
                if dist>ans:
                    ans=dist
                for v, w in list(graph.graph[cur]):
                    if v not in visited:
                        heapq.heappush(heap, Position(v, dist+w))
        if count==n:
            return ans
        else:
            return -1








