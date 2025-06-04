n, m=map(int, input().split())
graph=[[] for i in range(n)]
for i in range(m):
    ini, fin=map(int, input().split())
    graph[ini].append(fin)
def has_circle(graph, n):
    visited=set()
    trace=set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            trace.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                else:
                    if neighbor in trace:
                        return True
            trace.remove(node)
        return False

    for i in range(n):
        if dfs(i):
            return True

    return False

if has_circle(graph, n):
    print("Yes")
else:
    print("No")

