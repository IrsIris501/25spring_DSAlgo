import heapq
ans = -1
k = int(input())
n = int(input())
r = int(input())
adj = [[] for i in range(n)]
for i in range(r):
    s, d, l, t = map(int, input().split())
    adj[s-1].append((d-1, l, t))
heap = [(0, 0, 0)]
visited = set()
while heap:
    dist, toll, pos = heapq.heappop(heap)
    if pos == n-1:
        ans = dist
        break
    visited.add(pos)
    for d, l, t in adj[pos]:
        if t + toll <= k:
            heapq.heappush(heap, (dist + l, t + toll, d))
print(ans)