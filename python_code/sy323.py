from collections import deque
def bfs(maze, n, m, start_x, start_y, end_x, end_y):
    q=deque()
    q.append((start_x, start_y, 0))
    inq=set()
    inq.add((start_x, start_y))
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    while q:
        x, y, step=q.popleft()
        if (x, y)==(end_x, end_y):
            return step
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and maze[x+dx[i]][y+dy[i]]!='*' and (x+dx[i], y+dy[i]) not in inq:
                q.append((x+dx[i], y+dy[i], step+1))
                inq.add((x+dx[i], y+dy[i]))
    return -1

n, m=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(input()))
for i in range(n):
    for j in range(m):
        if maze[i][j]=='S':
            start_x=i
            start_y=j
        elif maze[i][j]=='T':
            end_x=i
            end_y=j
print(bfs(maze, n, m, start_x, start_y, end_x, end_y))





