from collections import deque
def bfs(maze, n, m):
    q=deque()
    q.append((0, 0, 0))
    inq=set()
    inq.add((0, 0))
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    while q:
        x, y, step=q.popleft()
        if (x, y)==(n-1, m-1):
            return step
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and not maze[x+dx[i]][y+dy[i]] and (x+dx[i], y+dy[i]) not in inq:
                q.append((x+dx[i], y+dy[i], step+1))
                inq.add((x+dx[i], y+dy[i]))
    return -1

n, m=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))

print(bfs(maze, n, m))





