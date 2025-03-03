class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        prepro=[]
        sufpro=[]
        for i in range(len(grid)):
            prepro.append([])
            for j in range(len(grid[i])):
                if j!=0:
                    prepro[i].append((prepro[i][j-1]*grid[i][j])%12345)
                else:
                    prepro[i].append(grid[i][j]%12345)
        for i in range(len(grid)):
            sufpro.append([])
            for j in range(len(grid[i])-1, 0, -1):
                if j!=len(grid[i])-1:
                    sufpro[i].append((grid[i][j]*sufpro[i][len(grid[i])-2-j])%12345)
                else:
                    sufpro[i].append(grid[i][j]%12345)
            sufpro[i].reverse()
        ans=[]
        for i in range(len(grid)):
            ans.append([])
            start=1
            for k in range(len(grid)):
                if k != i:
                    start = (start * prepro[k][-1]) % 12345
            for j in range(len(grid[i])):
                temp=start
                if len(grid[i])>1:
                    if j!=0 and j!=len(grid[i])-1:
                        temp=(temp*prepro[i][j-1]*sufpro[i][j])%12345
                    elif j==0:
                        temp=(temp*sufpro[i][j])%12345
                    else:
                        temp=(temp*prepro[i][j-1])%12345
                ans[i].append(temp)
        return ans

s=Solution()
n, m=map(int, input().split())
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))
print(s.constructProductMatrix(grid))