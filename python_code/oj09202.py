from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    count = 0
    graph = defaultdict(set)
    reverse_graph = defaultdict(set)
    n, m = map(int, input().split())
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].add(y)
        reverse_graph[y].add(x)
    visited = set()
    q = deque()
    for i in range(n):
        if not reverse_graph[i]:
            q.append(i)
    while q:
        cur = q.popleft()
        count += 1
        for i in graph[cur]:
            reverse_graph[i].remove(cur)
            if not reverse_graph[i]:
                q.append(i)
    if count != n:
        print("Yes")
    else:
        print('No')


