import bisect


class DisjointSet:
    def __init__(self, n):
        self.parent=list(range(n))
        self.rank=[0 for i in range(n)]
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x=self.parent[x]
        root_y=self.parent[y]
        if root_x!=root_y:
            if self.rank[root_x]>self.rank[root_y]:
                self.parent[root_y]=root_x
            elif self.rank[root_y]>self.rank[root_x]:
                self.parent[root_x]=root_y
            else:
                self.parent[root_x]=root_y
                self.rank[root_y]+=1


class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        ds=DisjointSet(n)
        m=0
        for i in range(n):
            b=bisect.bisect_right(nums, nums[i]+maxDiff)-1
            for j in range(max(m, i), b+1):
                ds.union(i, j)
            m=max(m, b)
        for i in range(n):
            ds.find(i)
        ans=[]
        for x, y in queries:
            ans.append(ds.find(x)==ds.find(y))
        return ans

