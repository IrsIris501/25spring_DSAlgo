# Assignment #C: 202505114 Mock Exam

Updated 1504 GMT+8 May 19, 2025

2025 spring, Complied by <mark>陈虹骏 物理学院</mark>



> **说明：**
>
> 1. **⽉考**：AC4<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E06364: 牛的选举

http://cs101.openjudge.cn/practice/06364/

思路：



代码：

```python
n, k=map(int, input().split())
a=[]
b=[]
for i in range(n):
    ai, bi=map(int, input().split())
    a.append((i+1, ai))
    b.append(bi)
a.sort(reverse=True, key=lambda x:x[1])
a=a[0:k]
b_valid=[]
for i in a:
    b_valid.append((i[0], b[i[0]-1]))
b_valid.sort(reverse=True, key=lambda x:x[1])
print(b_valid[0][0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250515173655.png)



### M04077: 出栈序列统计

http://cs101.openjudge.cn/practice/04077/

思路：



代码：

```python
n=int(input())
count=0
def dfs(cur, stack, out):
    global count
    if out==n:
        count+=1
        return
    if stack:
        a=stack.pop()
        dfs(cur, stack, out+1)
        stack.append(a)
    if cur<n:
        stack.append(cur)
        dfs(cur+1, stack, out)
        stack.pop()

dfs(0, [], 0)
print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250515173732.png)



### M05343:用队列对扑克牌排序

http://cs101.openjudge.cn/practice/05343/

思路：



代码：

```python
n=int(input())
cards=input().split()
q1=[[] for i in range(9)]
for i in range(n):
    q1[int(cards[i][1])-1].append(cards[i])
stack1=[]
for i in range(9):
    print(f'Queue{i+1}:', end='')
    print(*q1[i])
    stack1+=q1[i]
q2=[[] for i in range(4)]
for i in stack1:
    q2[ord(i[0])-ord('A')].append(i)
ans=[]
for i in range(4):
    print('Queue'+chr(i+ord('A'))+':', end='')
    print(*q2[i])
    ans+=q2[i]
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250515173849.png)



### M04084: 拓扑排序

http://cs101.openjudge.cn/practice/04084/

思路：



代码：

```python
from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.graph=defaultdict(set)
        self.reverse=defaultdict(set)
        self.num=n
    def add_edge(self, a, b):
        self.graph[a].add(b)
        self.reverse[b].add(a)
    def topological_order(self):
        visited=set()
        count=0
        stack=[]
        while count<self.num:
            for i in range(1, self.num+1):
                if i not in visited and self.reverse[i]==set():
                    stack.append(i)
                    count+=1
                    visited.add(i)
                    for j in range(1, self.num+1):
                        if i in self.reverse[j]:
                            self.reverse[j].remove(i)
                    break
        return stack



v, a=map(int, input().split())
graph=Graph(v)
for i in range(a):
    start, fin=map(int, input().split())
    graph.add_edge(start, fin)
temp=graph.topological_order()
ans=[]
for i in temp:
    ans.append('v'+str(i))
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250515173757.png)



### M07735:道路

Dijkstra, http://cs101.openjudge.cn/practice/07735/

思路：



代码：

```python
import heapq
ans = -1
k = int(input())
n = int(input())
r = int(input())
adj = [[] for i in range(n)]
for i in range(r):
    s, d, l, t = map(int, input().split())
    adj[s-1].append((d-1, l, t))
heap = [(0, 0, 0)]
visited = set()
while heap:
    dist, toll, pos = heapq.heappop(heap)
    if pos == n-1:
        ans = dist
        break
    visited.add(pos)
    for d, l, t in adj[pos]:
        if t + toll <= k:
            heapq.heappush(heap, (dist + l, t + toll, d))
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250519150345.png)



### T24637:宝藏二叉树

dp, http://cs101.openjudge.cn/practice/24637/

思路：



代码：

```python
n=int(input())
value=list(map(int, input().split()))
dp1=[0 for i in range(n)]
dp2=[0 for i in range(n)]

for i in range(n-1, -1, -1):
    temp=[]
    left=i*2+1
    right=i*2+2
    dp1[i]+=value[i]
    if left<n:
        dp1[i]+=dp2[left]
    if right<n:
        dp1[i]+=dp2[right]
    if left<n:
        dp2[i]+=max(dp2[left], dp1[left])
    if right<n:
        dp2[i]+=max(dp2[right], dp1[right])
print(max(dp1[0], dp2[0]))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250515201654.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

最后一题刚开始看成了两个如果是同一个节点的左右子节点就不能同时选，于是直接想着先解决子问题，结果写完发现不对，于是一直在想怎么递归做，根本就没想到dp









