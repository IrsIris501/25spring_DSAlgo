import sys
sys.setrecursionlimit(1000000)
class DisjointSet:
    def __init__(self, num, c):
        self.pre = [i for i in range(num)]
        self.rank = c
    def find(self, x):
        if self.pre[x] != x:
            self.pre[x] = self.find(self.pre[x])
        return self.pre[x]
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:  # 已经在同一集合中
            return

        # 按秩合并
        if self.rank[x_root] > self.rank[y_root]:
            self.pre[x_root] = y_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.pre[y_root] = x_root
        else:
            self.pre[y_root] = x_root

n, m = map(int, input().split())
c = list(map(int, input().split()))
disjoint_set = DisjointSet(n, c)

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    disjoint_set.union(x, y)

ans = 0
visited = set()
for i in range(n):
    parent = disjoint_set.find(i)
    if parent not in visited:
        visited.add(parent)
        ans += c[parent]
print(ans)
