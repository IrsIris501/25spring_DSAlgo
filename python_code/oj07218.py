from collections import deque

t=int(input())
for _ in range(t):
    r, c=map(int, input().split())
    maze=[]
    for i in range(r):
        maze.append(list(input()))
    def find_start(maze):
        for i in range(r):
            for j in range(c):
                if maze[i][j]=='S':
                    return (i, j)
    start_x, start_y=find_start(maze)
    q=deque()
    q.append((start_x, start_y, 0))
    visited=set()
    visited.add((start_x, start_y))
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    can_reach=False
    while q:
        x, y, step=q.popleft()
        if maze[x][y]=='E':
            print(step)
            can_reach=True
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and (nx, ny) not in visited and maze[nx][ny]!='#':
                q.append((nx, ny, step+1))
                visited.add((nx, ny))

    if not can_reach:
        print('oop!')