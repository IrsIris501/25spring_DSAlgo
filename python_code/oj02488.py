# pylint: skip-file
dx=[-1, 1, -2, 2, -2, 2, -1, 1]
dy=[-2, -2, -1, -1, 1, 1, 2, 2]
def avail(x, y, p, q, visited):
    return 0<=x<p and 0<=y<q and not visited[x][y]

def dfs(x: int, y: int, path:str, p, q):
    global visited
    global can_reach
    if can_reach:
        return
    path+=chr(y+65)+str(x+1)
    full=True
    for i in range(p):
        if False in visited[i]:
            full=False
            break
    if full:
        can_reach=True
        print(path)
        return
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if avail(nx, ny, p, q, visited):
            visited[nx][ny]=True
            dfs(nx, ny, path, p, q)
            visited[nx][ny]=False




n=int(input())
for _ in range(n):
    p, q=map(int, input().split())
    print('Scenario #'+str(_+1)+':')

    can_reach=False
    for i in range(p):
        for j in range(q):
            visited = [[False for x in range(q)] for y in range(p)]
            visited[i][j] = True
            dfs(i, j, '', p, q)
            if can_reach:
                break
        if can_reach:
            break
    if not can_reach:
        print('impossible')
    print()