# Assignment #7: 20250402 Mock Exam

Updated 1529 GMT+8 Apr 4, 2025

2025 spring, Complied by <mark>物理学院 陈虹骏</mark>



> **说明：**
>
> 1. **⽉考**：<mark>AC5</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E05344:最后的最后

http://cs101.openjudge.cn/practice/05344/



思路：感觉循环链表不是很熟悉，还是使用deque



代码：

```python
from collections import deque

n, k=map(int, input().split())
q=[i for i in range(1, n+1)]
q=deque(q)
dead=[]
while len(q)>1:
    for i in range(k-1):
        q.append(q.popleft())
    dead.append(q.popleft())
print(*dead)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250403145113.png)



### M02774: 木材加工

binary search, http://cs101.openjudge.cn/practice/02774/



思路：



代码：

```python
n, k=map(int, input().split())
log=[]
left=0
right=10001
for i in range(n):
    log.append(int(input()))
if sum(log)<k:
    print(0)
else:

    while left+1<right:
        mid=(left+right)//2
        count=0
        for i in log:
            count+=i//mid
        if count<k:
            right=mid
        else:
            left=mid
    print(left)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250403145228.png)



### M07161:森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/



思路：由bfs遍历得到的层序遍历就要在bfs成一棵树！



代码：

```python
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, s, num):
        self.val=s
        self.children=[]
        self.num=num

def build_tree(stack):
    q=deque()
    item, count=stack.popleft()
    tree=TreeNode(item, count)
    q.append(tree)
    while stack and q:
        current_tree=q.popleft()
        for i in range(current_tree.num):
            item, count=stack.popleft()
            child=TreeNode(item, count)
            current_tree.children.append(child)
            q.append(child)
    return tree

def post_order(tree: TreeNode):
    global ans
    for i in tree.children:
        post_order(i)
    ans.append(tree.val)

t=int(input())
ans=[]
for i in range(t):
    stack=deque()
    temp_stack=input().split()
    for j in range(len(temp_stack)):
        if ord('A')<=ord(temp_stack[j])<=ord('Z'):
            temp = temp_stack[j]
        else:
            stack.append((temp, int(temp_stack[j])))
    tree=build_tree(stack)
    post_order(tree)
print(*ans)



```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250404152853.png)



### M18156:寻找离目标数最近的两数之和

two pointers, http://cs101.openjudge.cn/practice/18156/



思路：



代码：

```python
t=int(input())
s=list(map(int, input().split()))
s.sort()
left=0
right=len(s)-1
closest=-10000
flag=0
while right>=left+1:
    if s[left]+s[right]>t:
        if abs(s[left]+s[right]-t)<abs(closest-t) or (abs(s[left]+s[right]-t)==abs(closest-t) and s[left]+s[right]<t):
            closest=s[left]+s[right]
        right-=1
        if right==left:
            print(closest)
            flag=1
            break
    elif s[left]+s[right]<t:
        if abs(s[left]+s[right]-t)<abs(closest-t) or (abs(s[left]+s[right]-t)==abs(closest-t) and s[left]+s[right]<t):
            closest=s[left]+s[right]
        left+=1
        if right==left:
            print(closest)
            flag=1
            break
    else:
        print(t)
        flag=1
        break
if not flag:
    print(closest)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250403145308.png)



### M18159:个位为 1 的质数个数

sieve, http://cs101.openjudge.cn/practice/18159/



思路：直接把codeforces 230B T-Prime 的代码copy过来



代码：

```python
import math
primes=[]
numbers=[True]*(10**4+1)
numbers[0]=False
numbers[1]=False
def sieve(numbers):
    for i in range(2, int(1e4+1)):
        if numbers[i]:
            primes.append(i)
        for j in range(len(primes)):
            if i*primes[j]>int(1e4):
                break
            numbers[i*primes[j]]=False
            if i%primes[j]==0:
                break
sieve(numbers)

t=int(input())
for i in range(1, t+1):
    n=int(input())
    print('Case'+str(i)+':')
    j=0
    l=[]
    while j*10+1<n:
        if numbers[j*10+1]:
            l.append(j*10+1)
        j+=1
    if l:
        print(*l)
    else:
        print('NULL')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250403145410.png)



### M28127:北大夺冠

hash table, http://cs101.openjudge.cn/practice/28127/



思路：



代码：

```python
t=int(input())
teams=set()
map_table=dict()
status=[]
for i in range(t):
    team, prob, stat=input().split(',')
    if team in teams:
        pointer=map_table[team]
        if stat=='yes' and status[pointer][ord(prob)-ord('A')]==False:
            status[pointer][ord(prob)-ord('A')]=True
            status[pointer][26]+=1
        status[pointer][27]+=1
    else:
        teams.add(team)
        status.append([False for i in range(26)]+[0, 0]+[team])
        pointer=len(status)-1
        map_table[team]=pointer
        if stat=='yes' and status[pointer][ord(prob)-ord('A')]==False:
            status[pointer][ord(prob)-ord('A')]=True
            status[pointer][26]+=1
        status[pointer][27]+=1
status.sort(key=lambda x:(-x[26], x[27], x[28]))
i=0
while i<12 and i<len(status):
    print(i+1, status[i][28], status[i][26], status[i][27])
    i+=1
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250403145442.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

俳句：

刚会二叉树

考试就考多叉树

直接绷不住



评价：最难绷









