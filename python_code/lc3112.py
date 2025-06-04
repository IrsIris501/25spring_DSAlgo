import heapq
from collections import defaultdict


class Point:
    def __init__(self, pos, time):
        self.pos = pos
        self.time = time
    def __gt__(self, other):
        return self.time > other.time

class Graph:
    def __init__(self, n):
        self.num = n
        self.graph = defaultdict(list)
    def add_edge(self, u, v, length):
        self.graph[u].append((v, length))
        self.graph[v].append((u, length))

class Solution:
    def minimumTime(self, n: int, edges: list[list[int]], disappear: list[int]) -> list[int]:
        ans = [-1 for i in range(n)]
        graph = Graph(n)
        for u, v, length in edges:
            graph.add_edge(u, v, length)
        heap = [Point(0, 0)]
        visited = set()
        while heap and len(visited) < n:
            point = heapq.heappop(heap)
            cur_pos = point.pos
            cur_time = point.time
            if cur_time < disappear[cur_pos] and cur_pos not in visited:
                ans[cur_pos] = cur_time
                visited.add(cur_pos)
                for head, length in graph.graph[cur_pos]:
                    if head not in visited:
                        heapq.heappush(heap, Point(head, cur_time + length))
            elif cur_time >= disappear[cur_pos] and cur_pos not in visited:
                visited.add(cur_pos)
        return ans



