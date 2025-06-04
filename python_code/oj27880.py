from collections import defaultdict
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[yr] > self.rank[xr]:
            self.parent[xr] = yr
        else:
            self.parent[xr] = yr
            self.rank[yr] += 1



n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((c, u, v))
edges.sort()
disjoint_set = DisjointSet(n)
max_len = 0
for length, a, b in edges:
    if disjoint_set.find(a) != disjoint_set.find(b):
        max_len = max(max_len, length)
        disjoint_set.union(a, b)
    if len(set(disjoint_set.parent)) == 1:
        break
print(n-1, max_len)
