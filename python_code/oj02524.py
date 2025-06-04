class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # 初始化每个元素的父节点为自己
        self.rank = [0] * n  # 初始化每个集合的秩为0

    def find(self, x):
        """查找x的根节点，带有路径压缩优化"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        """合并x和y所在的集合，带有按秩合并优化"""
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:  # 已经在同一集合中
            return

        # 按秩合并
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

count = 0
while True:
    count += 1
    n, m = map(int, input().split())
    if n == 0:
        break
    disjoint_set = DisjointSet(n)
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        disjoint_set.union(a, b)
    visited = set()
    for i in range(n):
        temp = disjoint_set.find(i)
        if temp not in visited:
            visited.add(temp)
    print(f'Case {count}: {len(visited)}')