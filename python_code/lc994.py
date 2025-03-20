


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque
        dx=[1, 0, -1, 0]
        dy=[0, 1, 0, -1]
        q=deque()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    count+=1
                elif grid[i][j]==2:
                    q.append((0, i, j))
        nowtime=0
        if count==0:
            return 0
        while q:
            time, x, y=q.popleft()
            nowtime=time+1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                    q.append((nowtime, nx, ny))
                    grid[nx][ny]=2
                    count-=1
                    if count==0:
                        return nowtime
        return -1

s=Solution()
n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))
print(s.orangesRotting(grid))





