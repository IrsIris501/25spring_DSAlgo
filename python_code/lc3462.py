class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        temp=[]
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            temp.extend(grid[i][:limits[i]])
        temp.sort(reverse=True)
        return sum(temp[:k])

s=Solution()
n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))
limits=list(map(int, input().split()))
k=int(input())
print(s.maxSum(grid, limits, k))