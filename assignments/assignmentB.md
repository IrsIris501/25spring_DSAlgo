# Assignment #B: 图为主

Updated 1527 GMT+8 May 7, 2025

2025 spring, Complied by <mark>物理学院 陈虹骏</mark>



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

### E07218:献给阿尔吉侬的花束

bfs, http://cs101.openjudge.cn/practice/07218/

思路：



代码：

```python
from collections import deque

t=int(input())
for _ in range(t):
    r, c=map(int, input().split())
    maze=[]
    for i in range(r):
        maze.append(list(input()))
    def find_start(maze):
        for i in range(r):
            for j in range(c):
                if maze[i][j]=='S':
                    return (i, j)
    start_x, start_y=find_start(maze)
    q=deque()
    q.append((start_x, start_y, 0))
    visited=set()
    visited.add((start_x, start_y))
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    can_reach=False
    while q:
        x, y, step=q.popleft()
        if maze[x][y]=='E':
            print(step)
            can_reach=True
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and (nx, ny) not in visited and maze[nx][ny]!='#':
                q.append((nx, ny, step+1))
                visited.add((nx, ny))

    if not can_reach:
        print('oop!')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250505140829.png)



### M3532.针对图的路径存在性查询I

disjoint set, https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

思路：感觉并查集的方法就比较慢



代码：

```python
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


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250505150657.png)



### M22528:厚道的调分方法

binary search, http://cs101.openjudge.cn/practice/22528/

思路：



代码：

```python
score=[float(x) for x in input().split()]
n=len(score)

def adjust(a, x):
    return a*x+1.1**(a*x)
left=0
right=1000000000
while right-left!=1:
    mid=(left+right)//2
    count=0
    for i in score:
        if adjust(mid/1000000000, i)>=85:
            count+=1
    if count>=0.6*n:
        right=mid
    else:
        left=mid
print(right)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250505141842.png)



### Msy382: 有向图判环 

dfs, https://sunnywhy.com/sfbj/10/3/382

思路：



代码：

```python
n, m=map(int, input().split())
graph=[[] for i in range(n)]
for i in range(m):
    ini, fin=map(int, input().split())
    graph[ini].append(fin)
def has_circle(graph, n):
    visited=set()
    trace=set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            trace.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                else:
                    if neighbor in trace:
                        return True
            trace.remove(node)
        return False

    for i in range(n):
        if dfs(i):
            return True

    return False

if has_circle(graph, n):
    print("Yes")
else:
    print("No")


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250505155824.png)



### M05443:兔子与樱花

Dijkstra, http://cs101.openjudge.cn/practice/05443/

思路：



代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250506142217.png)



### T28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

oj05443吐槽：样例给出的路线是在干什么？东京大回环了属于是

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-05%20152530.png)

正解：![](https://raw.githubusercontent.com/IrsIris501/img/main/20250505152945.png)













