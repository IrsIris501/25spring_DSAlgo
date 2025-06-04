from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
restricted = set(map(int, input().split()))
q = deque()
q.append(0)
visited = set()
visited.add(0)
while q:
    cur = q.popleft()

    for i in graph[cur]:
        if i not in visited and i not in restricted:
            q.append(i)
            visited.add(i)
print(len(visited))
