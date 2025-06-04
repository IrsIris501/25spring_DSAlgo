import heapq
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
visited = set()
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
heap = [(0, 0)]

while heap:
    dist, pos = heapq.heappop(heap)
    if pos not in visited:
        if pos == n-1:
            print(dist)
            break

        visited.add(pos)
        for next_pos, length in graph[pos]:
            if next_pos not in visited:
                heapq.heappush(heap, (dist + length, next_pos))




