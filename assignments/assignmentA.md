# Assignment #A: Graph starts

Updated 1442 GMT+8 Apr 29, 2025

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

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：



代码：

```python
class Vertex:
    def __init__(self, key):
        self.id=key
        self.neighbor=set()

class Graph:
    def __init__(self, n):
        self.vert_dict=dict()
        for i in range(n):
            self.vert_dict[i]=Vertex(i)
    def add_edge(self, a, b):
        self.vert_dict[a].neighbor.add(self.vert_dict[b])
        self.vert_dict[b].neighbor.add(self.vert_dict[a])

n, m=map(int, input().split())
graph=Graph(n)
for _ in range(m):
    a, b=map(int, input().split())
    graph.add_edge(a, b)

d=[[0 for i in range(n)] for j in range(n)]
a=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    d[i][i]=len(graph.vert_dict[i].neighbor)
for i in range(n):
    for j in range(i+1, n):
        if graph.vert_dict[i] in graph.vert_dict[j].neighbor:
            a[i][j]=1
            a[j][i]=1

l=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        l[i][j]=d[i][j]-a[i][j]
for i in range(n):
    print(*l[i])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250429085355.png)



### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：使用bfs，感觉和backtracking的区别就是如何遍历这个树



代码：

```python
from collections import deque


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]
        q=deque()
        q.append([nums[0]])
        q.append([])
        cur=1
        count=0
        while q:
            temp=q.popleft()
            count+=1
            if cur!=len(nums):
                q.append(temp+[nums[cur]])
                q.append(temp)
                if count==2**cur:
                    cur+=1
                    count=0
            else:
                q.append(temp)
                break
        return list(q)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250426144739.png)



### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：



代码：

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        global ans
        if not digits:
            return []
        map_dict=dict()
        for i in range(2, 7):
            map_dict[i]=[chr(ord('a')+3*(i-2)), chr(ord('a')+3*(i-2)+1), chr(ord('a')+3*(i-2)+2)]
        map_dict[7]=['p', 'q', 'r', 's']
        map_dict[8]=['t', 'u', 'v']
        map_dict[9]=['w', 'x', 'y', 'z']
        
        ans=[]
        def dfs(digits: str, cur=''):
            global ans
            temp=digits[0]
            if len(digits)==1:
                for i in map_dict[int(temp)]:
                    ans.append(cur+i)
                return
            else:
                for i in map_dict[int(temp)]:
                    dfs(digits[1::], cur+i)


        dfs(digits)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250429082513.png)



### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：



代码：

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

t=int(input())
for _ in range(t):
    n=int(input())
    root=Trie()
    nums=[]
    for i in range(n):
        nums.append(input())
    avail=True
    for i in nums:
        avail=root.insert_check(i)
        if not avail:
            print('NO')
            break
    if avail:
        print('YES')



```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250429141751.png)



### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：一开始用的是Graph+Vertex OOP方法，但是要pypy才能AC，于是使用了群里的字典的方法，该方法节约时间的地方应该在于没有管那些没有走到过的节点的边



代码：

```python
from collections import deque, defaultdict



n=int(input())
words=[]
for i in range(n):
    words.append(input())
start, end=input().split()

pattern_map=defaultdict(list)
for word in words:
    for i in range(4):
        pattern=word[:i]+'*'+word[i+1:]
        pattern_map[pattern].append(word)


q=deque()
q.append(start)
prev={start: None}
visited=set([start])
can_reach=False
while q:
    cur=q.popleft()
    if cur==end:
        path=[]
        while prev[cur]:
            path.append(cur)
            cur=prev[cur]
        path.append(start)
        path.reverse()
        print(*path)
        can_reach=True
        break
    for i in range(4):
        pattern=cur[:i]+'*'+cur[i+1:]
        for next in pattern_map[pattern]:
            if next==cur:
                continue
            else:
                if next not in visited:
                    q.append(next)
                    visited.add(next)
                    prev[next]=cur


if not can_reach:
    print('NO')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250429094842.png)



### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：



代码：

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        global solutions
        def is_safe(col, board):
            for i in range(len(board)):
                if board[i]==col:
                    return False
                if abs(col-board[i])==abs(len(board)-i):
                    return False
            return True

        solutions=[]

        def backtrack(board, n):
            global solutions
            if len(board)==n:
                temp=[]
                for i in range(n):
                    temp.append('.'*board[i]+'Q'+'.'*(n-board[i]-1))
                solutions.append(temp)
                return
            for i in range(n):
                if is_safe(i, board):
                    backtrack(board+[i], n)

        backtrack([], n)
        return solutions
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250429144212.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉这周除了前缀树和图的OOP要学习一下以外，题目难度不大

争取五一期间做一点每日选做









