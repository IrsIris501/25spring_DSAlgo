class DisjointSet:
    def __init__(self, num):
        self.pre = [i for i in range(num)]
        self.rank = [0 for i in range(num)]
    def find(self, x):
        if self.pre[x] != x:
            self.pre[x] = self.find(self.pre[x])
        return self.pre[x]
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return

        if self.rank[xr] > self.rank[yr]:
            self.pre[yr] = xr
        elif self.rank[yr] > self.rank[xr]:
            self.pre[xr] = yr
        else:
            self.pre[yr] = xr
            self.rank[xr] += 1


n = int(input())
neq = []
disjoint_set = DisjointSet(26)

for i in range(n):
    s = input()
    if s[1] == "!":
        neq.append((ord(s[0]) - ord('a'), ord(s[-1]) - ord('a')))
    else:
        disjoint_set.union(ord(s[0]) - ord('a'), ord(s[-1]) - ord('a'))

def judge(neq, disjoint_set):
    for a, b in neq:
        if disjoint_set.find(a) == disjoint_set.find(b):
            return False
    return True

print("True" if judge(neq, disjoint_set) else "False")