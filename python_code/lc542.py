


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        from collections import deque
        dx=[1, -1, 0, 0]
        dy=[0, 0, 1, -1]

        n=len(mat)
        m=len(mat[0])
        q=deque()
        ans=[[-1 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    ans[i][j]=0
                    q.append((0, i, j))
        while q:
            distance, x, y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and ans[nx][ny]==-1:
                    ans[nx][ny]=distance+1
                    q.append((distance+1, nx, ny))
        return ans

s=Solution()
n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int, input().split())))
ans=s.updateMatrix(mat)
for i in range(n):
    print(*ans[i])


