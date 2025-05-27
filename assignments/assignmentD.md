# Assignment #D: 图 & 散列表

Updated 1632 GMT+8 May 27, 2025

2025 spring, Complied by <mark>陈虹骏 物理学院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### M17975: 用二次探查法建立散列表

http://cs101.openjudge.cn/practice/17975/

<mark>需要用这样接收数据。因为输入数据可能分行了，不是题面描述的形式。OJ上面有的题目是给C++设计的，细节考虑不周全。</mark>

```python
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
```



思路：键会重复是真的阴间，不过想想其实也有道理，就类似于set.add(...)如果里面已经有了就不管了



代码：

```python

import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
def insert_element(hash_table, ele: int, m):
    pos = ele % m
    if not hash_table[pos] or hash_table[pos] == ele:
        hash_table[pos] = ele
        return pos
    else:
        k = 1
        while True:
            npos = (pos + k * k) % m
            if not hash_table[npos] or hash_table[npos] == ele:
                hash_table[npos] = ele
                return npos
            npos = (pos - k * k) % m
            if not hash_table[npos] or hash_table[npos] == ele:
                hash_table[npos] = ele
                return npos
            k += 1





l = [None for i in range(m)]
ans = []
for i in num_list:
    temp = insert_element(l, i, m)
    ans.append(temp)
print(*ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250527155115.png)



### M01258: Agri-Net

MST, http://cs101.openjudge.cn/practice/01258/

思路：多组测试样例没看到，但是并没有每行不得多于80个字符的奇怪限制



代码：

```python
while True:
    try:
        n = int(input())
    except EOFError:
        break
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    
    min_dist = [100010] + mat[0][1::]
    def find_min(l):
        temp = []
        for i in range(len(l)):
            temp.append((l[i], i))
        return min(temp)
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20250527163248420](C:\Users\Eric_\AppData\Roaming\Typora\typora-user-images\image-20250527163248420.png)



### M3552.网络传送门旅游

bfs, https://leetcode.cn/problems/grid-teleportation-traversal/

思路：



代码：

```python
from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        map_map = [[] for i in range(26)]
        for i in range(n):
            for j in range(m):
                if ord('A') <= ord(matrix[i][j]) <= ord('Z'):
                    map_map[ord(matrix[i][j]) - ord('A')].append((i, j))
        q = deque([(0, 0, 0)])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = set()
        visited_gateway = set()
        while q:
            x, y, step = q.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                if x == n-1 and y == m-1:
                    return step
                if ord('A') <= ord(matrix[x][y]) <= ord('Z'):
                    if matrix[x][y] not in visited_gateway:
                        for i in range(n):
                            for j in range(m):
                                if matrix[i][j] == matrix[x][y] and (i, j) != (x, y) and (i, j) not in visited:
                                    q.appendleft((i, j, step))
                        visited_gateway.add(matrix[x][y])



                for i in range(4):
                    if (x + dx[i], y + dy[i]) not in visited and 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and matrix[x + dx[i]][y + dy[i]] != '#':
                        q.append((x + dx[i], y + dy[i], step + 1))
        return -1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250526175941.png)



### M787.K站中转内最便宜的航班

Bellman Ford, https://leetcode.cn/problems/cheapest-flights-within-k-stops/

思路：



代码：

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        flight_map=[[-1 for i in range(n)] for j in range(n)]
        f = [[-1 for i in range(n)] for j in range(k+1)]
        for fro, to, price in flights:
            flight_map[fro][to]=price
            if fro==src:
                f[0][to]=price
        for i in range(1, k+1):
            for j in range(n):
                min_price=10000000
                for l in range(n):
                    if flight_map[l][j]!=-1 and f[i-1][l]!=-1 and f[i-1][l]+flight_map[l][j]<min_price:
                        min_price=f[i-1][l]+flight_map[l][j]
                if min_price<10000000:
                    f[i][j]=min_price
        ans=10000000
        for i in range(k+1):
            if f[i][dst]!=-1 and f[i][dst]<ans:
                ans=f[i][dst]
        if ans<10000000:
            return ans
        else:
            return -1

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250524153452.png)



### M03424: Candies

Dijkstra, http://cs101.openjudge.cn/practice/03424/

思路：感觉题目描述里面应该再放一个所有c都>=0，不然Dijkstra应该就用不了，万幸这里确实有all c >= 0



代码：

```python
import heapq
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
visited = set()
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
heap = [(0, 0)]

while heap:
    dist, pos = heapq.heappop(heap)
    if pos not in visited:
        if pos == n-1:
            print(dist)
            break

        visited.add(pos)
        for next_pos, length in graph[pos]:
            if next_pos not in visited:
                heapq.heappush(heap, (dist + length, next_pos))





```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250524160813.png)



### M22508:最小奖金方案

topological order, http://cs101.openjudge.cn/practice/22508/

思路：



代码：

```python
from collections import defaultdict, deque


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

n, m=map(int, input().split())
graph=Graph(n)
for i in range(m):
    a, b=map(int, input().split())
    graph.add_edge(b, a)

stack=graph.topological_order()
ans=n*100
for i in stack:
    ans+=i[1]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250524153317.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>



学习了散列表和最小生成树，感觉数算课程的内容量真的比计概多不少，希望老师机考手下留情

另外，机考题目会有提示词吗？比如 MST/topological order 这些







