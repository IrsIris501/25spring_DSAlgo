# pylint: skip-file
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m  and not visited[x][y]

def traversal(visited):
    for i in visited:
        for j in i:
            if not j:
                return False
    return True

def dfs(x, y, visited):
    global count
    if traversal(visited):
        count+=1
        return
    for i in range(8):
        nextx = x + dx[i]
        nexty = y + dy[i]
        if is_valid(nextx, nexty):
            visited[nextx][nexty]=True
            dfs(nextx, nexty, visited)
            visited[nextx][nexty] = False

t=int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y]=True
    count=0
    dfs(x, y, visited)
    print(count)
