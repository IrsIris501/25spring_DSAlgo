from collections import defaultdict


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

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)

n, m = map(int, input().split())
disjoint_set = DisjointSet(n)
graph = Graph()
for i in range(m):
    u, v = map(int, input().split())
    disjoint_set.union(u, v)
    graph.add_edge(u, v)

def disconnected(disjoint_set, n):
    global stack
    father = disjoint_set.find(0)
    connected = True
    visited = set()
    visited.add(father)
    for i in range(1, n):
        if disjoint_set.find(i) != father:
            connected = False
            if disjoint_set.find(i) not in visited:
                stack.append(i)
                visited.add(disjoint_set.find(i))
    return connected

stack = [0]
connected = disconnected(disjoint_set, n)
print('connected:', end = '')
print('yes' if connected else 'no')


def find_circuit(pos, last, n):
    parent = [-1] * n
    visited = [False for i in range(n)]
    visited[pos] = True
    q = [(pos, last)]

    while q:
        pos, par = q.pop()
        visited[pos] = True
        parent[pos] = par
        for next_pos in graph.graph[pos]:
            if not visited[next_pos]:
                q.append((next_pos, pos))
            elif next_pos != par:
                return True
    return False

found = False

for i in stack:
    found = find_circuit(i, None, n)
    if found:
        break

print('loop:', end = '')
print('yes' if found else 'no')








