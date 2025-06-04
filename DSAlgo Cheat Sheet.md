# DSAlgo Cheat Sheet

<mark>陈虹骏 物理学院</mark>

Updated at 1327 UTC+8, 4 Jun, 2025

## 1. oj有自定义函数时出现奇怪的compile error

在代码第一行加

```python
# pylint: skip-file
```

## 2. 欧拉筛

O(n)

```python
import math
n=int(input())
primes=[]
#numbers=[True for i in range(int(1e6+1))]
numbers=[True]*(10**6+1)
numbers[0]=False
numbers[1]=False
def sieve(numbers):
    for i in range(2, int(1e6+1)):
        if numbers[i]:
            primes.append(i)
        for j in range(len(primes)):
            if i*primes[j]>int(1e6):
                break
            numbers[i*primes[j]]=False
            if i%primes[j]==0:
                break
sieve(numbers)
```

## 3. Dijkstra

兔子与樱花，记录路径的Dijkstra

```python
from heapq import *
from collections import defaultdict

p=int(input())
graph=dict()
places=[]

for i in range(p):
    temp=input()
    places.append(temp)
    graph[temp]=[]

q=int(input())
for i in range(q):
    ini, fin, l=input().split()
    l=int(l)
    graph[ini].append((l, fin))
    graph[fin].append((l, ini))

r=int(input())
for _ in range(r):
    path=defaultdict(list)
    dist_dict=dict()
    shortest=defaultdict(bool)
    start, end=input().split()
    if start==end:
        print(start)
        break
    heap=[]
    heappush(heap, (0, start))
    while heap:
        dist, pos=heappop(heap)
        if pos==end:
            path_ans=''
            for i in path[pos]:
                path_ans+=i[0]
                path_ans+='->('
                path_ans+=str(i[1])
                path_ans+=')->'
            path_ans+=end
            print(path_ans)
            break
        shortest[pos]=True
        for i in graph[pos]:
            length=i[0]
            npos=i[1]
            if dist+length<dist_dict.get(npos, 100000):
                dist_dict[npos]=dist+length
                heappush(heap, (dist+length, npos))
                path[npos]=path[pos]+[(pos, length)]
```

or 走山路，不记录路径

```python
from heapq import *
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def avail(nx, ny):
    if 0<=nx<m and 0<=ny<n and maze[nx][ny]!="#" and (nx, ny) not in save:
        return 1
    else:
        return 0

m, n, p=map(int, input().split())
maze=[]
for i in range(m):
    a=input().split()
    maze.append([])
    for j in a:
        if j=="#":
            maze[i].append(j)
        else:
            maze[i].append(int(j))
for _ in range(p):
    x0, y0, x, y=map(int, input().split())
    if maze[x0][y0]=="#" or maze[x][y]=="#":
        print("NO")
    else:
        save=set()
        heap=[]
        flag=1
        heappush(heap, (0, x0, y0))
        while heap!=[]:
            l, px, py=heappop(heap)
            save.add((px, py))
            for i in range(4):
                nx=px+dx[i]
                ny=py+dy[i]
                if avail(nx, ny):
                    heappush(heap, (l+abs(maze[px][py]-maze[nx][ny]), nx, ny))
            if px==x and py==y:
                print(l)
                flag=0
                break
        if flag:
            print("NO")
```



## 4. disjoint set

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # 初始化每个元素的父节点为自己
        self.rank = [0] * n          # 初始化每个集合的秩为0
    
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
```

## 5. MST 最小生成树

#### 5.1 Prim

white set

```python
from collections import defaultdict
n = int(input())
mat = [[100010 for i in range(n)] for j in range(n)]
for i in range(n-1):
    temp = input().split()
    pos = ord(temp[0]) - ord('A')
    mat[pos][pos] = 0
    m = int(temp[1])
    index = 2
    for j in range(m):
        pos2 = ord(temp[index]) - ord('A')
        index += 1
        length = int(temp[index])
        mat[pos][pos2] = length
        mat[pos2][pos] = length
        index += 1

def find_min(l):
    min_l, min_i = float('inf'), 0
    for i in range(len(l)):
        if l[i] < min_l:
            min_l = l[i]
            min_i = i
    return min_l, min_i
min_dist = [100010] + mat[0][1::]
white = set()
white.add(0)
ans = 0
for _ in range(n-1):
    dist, pos = find_min(min_dist)
    ans += dist
    white.add(pos)
    min_dist[pos] = 100010
    for i in range(n):
        if i not in white:
            min_dist[i] = min(min_dist[i], mat[i][pos])

print(ans)
```

#### 5.2 Kruskal

<mark>disjoint set</mark> + greedy, eg. 繁忙的厦门

```python
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
```

## 6. KMP算法

#### 6.1 生成最小匹配前缀长度序列LPS

```python
def compute_lps(s: str, n:int) -> list[int]:
    length = 0
    lps = [0 for i in range(n)]
    for i in range(1, n):
        while length > 0 and s[i] != s[length]:
            length = lps[length-1]
        if s[i] == s[length]:
            length += 1
            lps[i] = length
    return lps


```

#### 6.2 比较

```python
def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0  # indices for text and pattern
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                print("Pattern found at index", i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
```

## 7. topological sort

核心：入度为0就append进q

```python
class Graph:
    def __init__(self, n):
        self.graph=defaultdict(set)
        self.reverse_graph=defaultdict(set)
        self.num=n
    def add_edge(self, a, b):
        self.graph[a].add(b)
        self.reverse_graph[b].add(a)
    def topological_order(self):
        q=deque()
        stack=[]
        for i in range(self.num):
            if len(self.reverse_graph[i])==0:
                q.append((i, 0))
        while q:
            cur, layer=q.popleft()
            stack.append((cur, layer))
            for i in list(self.graph[cur]):
                self.reverse_graph[i].remove(cur)
                if self.reverse_graph[i]==set():
                    q.append((i, layer+1))
        return stack
```

另，无向图找环，使用迭代dfs

```python
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
```



## 8. tree dp

核心：dfs/bfs + dp

例如：打家劫舍

```python
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0, 0
            left1, left2 = dfs(node.left)
            right1, right2 = dfs(node.right)
            return left2 + right2 + node.val, max(left1, left2) + max(right1, right2)
        a, b = dfs(root)
        return max(a, b)
```

## 9. 前缀树

```python
class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children={}

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert_check(self, char):
        ptr=self.root
        for i in range(len(char)):
            if char[i] in ptr.children:
                ptr=ptr.children[char[i]]
                if ptr.is_end:
                    return False
            else:
                ptr.children[char[i]]=TrieNode()
                ptr=ptr.children[char[i]]
        if ptr.children:
            return False
        ptr.is_end=True
        return True
```

## 10. 前缀和

往往还有后缀和

含义就是先预处理算出prefix sum and/or suffix sum

## 11. stack

##### 11.1 中序转后序

```python
def suffixize(s):
    '''
    param s: string
    return: list
    '''
    symbols=['+', '-', '*', '/']
    prime={'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')':0}
    number=[]
    action=[]
    temp=''
    s=list(s)
    while s[-1]==' ':
        s.pop()
    s+=['end']
    for i in range(len(s)):
        if s[i] in symbols:
            if temp!='':
                number.append(temp)
                temp=''
            if action:
                while prime[action[-1]]>=prime[s[i]]:
                    number.append(action.pop())
                    if not action:
                        break
            action.append(s[i])
        elif s[i]=='(':
            if temp!='':
                number.append(temp)
                temp=''
            action.append(s[i])
        elif s[i]==')':
            if temp!='':
                number.append(temp)
                temp=''
            while action[-1]!='(':
                number.append(action.pop())
                if not action:
                    break
            action.pop()
        elif s[i]!='end':
            temp+=s[i]
        else:
            if temp!='':
                number.append(temp)
                temp=''
    while action:
        number.append(action.pop())
    return number
```

## 12. tree

前序遍历：根左右

中序遍历：左根右

后序遍历：左右根

层序遍历：bfs

## 13. merge sort

可以用来求逆序数

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global ans
    stack = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            stack.append(left[i])
            i += 1
            ans += j
        else:
            stack.append(right[j])
            j += 1
    if i < len(left):
        for k in range(i, len(left)):
            stack.append(left[k])
            ans += j
    elif j < len(right):
        stack += right[j:]
    return stack
```

## 14. Huffman Tree

用来给字母编码

```python
import heapq


class TreeNode:
    def __init__(self, weight, alphabet, left=None, right=None):
        self.weight=weight
        self.alphabet=alphabet
        self.left=left
        self.right=right
    def __lt__(self, other):
        if self.weight!=other.weight:
            return self.weight<other.weight
        else:
            temp1=sorted(self.alphabet)
            temp2=sorted(self.alphabet)
            return ord(temp1[0])<ord(temp2[0])

n=int(input())
heap=[]
for i in range(n):
    char, freq=input().split()
    freq=int(freq)
    heap.append(TreeNode(freq, {char}))
heapq.heapify(heap)
while len(heap)>1:
    t1=heapq.heappop(heap)
    t2=heapq.heappop(heap)
    heapq.heappush(heap, TreeNode(t1.weight+t2.weight, t1.alphabet | t2.alphabet, t1, t2))
huffman_tree=heapq.heappop(heap)
```

