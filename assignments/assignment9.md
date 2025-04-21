# Assignment #9: Huffman, BST & Heap

Updated 1522 GMT+8 Apr 21, 2025

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

### LC222.完全二叉树的节点个数

bfs, dfs, binary + greedy,  https://leetcode.cn/problems/count-complete-tree-nodes/

如果用bfs写是简单级别，其他方法是中级难度。

思路：



代码：

```python
class Solution:
    '''
    bfs method
    def countNodes(self, root: TreeNode) -> int:
        ans=0
        if not root:
            return ans
        q=deque()
        q.append(root)
        while q:
            pos=q.popleft()
            ans+=1
            if pos.left:
                q.append(pos.left)
            if pos.right:
                q.append(pos.right)
        return ans
    '''

    def countNodes(self, root: TreeNode) -> int:
        '''
        binary search
        '''
        h=0
        if not root:
            return 0
        q=deque()
        q.append(root)
        while q:
            pos=q.popleft()
            h+=1
            if pos.left:
                q.append(pos.left)
        left=2**(h-1)
        right=2**h
        while right-left!=1:
            mid=(left+right)//2
            mid_bin=str(bin(mid))
            i=3
            pos=root
            avail=True
            while i<len(mid_bin):
                if int(mid_bin[i]):
                    if pos.right:
                        pos=pos.right
                        i+=1
                    else:
                        avail=False
                        break
                else:
                    if pos.left:
                        pos=pos.left
                        i+=1
                    else:
                        avail=False
                        break
            if avail:
                left=mid
            else:
                right=mid
        return left
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-17%20192619.png)



### LC103.二叉树的锯齿形层序遍历

bfs, https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

思路：



代码：

```python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append((root, 1))
        cur_level=0
        while q:
            pos, level=q.popleft()
            if level>cur_level:
                cur_level=level
                ans.append([])
            ans[-1].append(pos.val)
            if pos.left:
                q.append((pos.left, level+1))
            if pos.right:
                q.append((pos.right, level+1))
        for i in range(len(ans)):
            if i%2:
                ans[i].reverse()
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250417194423.png)



### M04080:Huffman编码树

greedy, http://cs101.openjudge.cn/practice/04080/

思路：



代码：

```python
import heapq
from collections import deque


class TreeNode:
    def __init__(self, val, count=0, left=None, right=None):
        self.val=val
        self.count=count
        self.left=left
        self.right=right
    def __lt__(self, other):
        return self.val<other.val

n=int(input())
weight=list(map(int, input().split()))
heap=[]
for i in range(len(weight)):
    heap.append(TreeNode(weight[i], count=1))
heapq.heapify(heap)
while len(heap)>1:
    t1=heapq.heappop(heap)
    t2=heapq.heappop(heap)
    temp=TreeNode(t1.val+t2.val, count=0, left=t1, right=t2)
    heapq.heappush(heap, temp)
huffman_tree=heapq.heappop(heap)
q=deque()
q.append((huffman_tree, 0))
ans=0
while q:
    pos, layer=q.popleft()
    if pos.count:
        ans+=pos.val*layer
    if pos.left:
        q.append((pos.left, layer+1))
    if pos.right:
        q.append((pos.right, layer+1))
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250418144407.png)



### M05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/

思路：



代码：

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

nums=list(map(int, input().split()))
in_tree_set=set()
bst=TreeNode(nums[0])
in_tree_set.add(nums[0])
for i in range(1, len(nums)):
    if nums[i] in in_tree_set:
        continue

    pos=bst
    while True:
        if nums[i]>pos.val:
            if pos.right:
                pos=pos.right
            else:
                pos.right=TreeNode(nums[i])
                break
        else:
            if pos.left:
                pos=pos.left
            else:
                pos.left=TreeNode(nums[i])
                break
    in_tree_set.add(nums[i])

q=deque()
q.append(bst)
ans=[]
while q:
    pos=q.popleft()
    ans.append(pos.val)
    if pos.left:
        q.append(pos.left)
    if pos.right:
        q.append(pos.right)
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250418150243.png)



### M04078: 实现堆结构

手搓实现，http://cs101.openjudge.cn/practice/04078/

类似的题目是 晴问9.7: 向下调整构建大顶堆，https://sunnywhy.com/sfbj/9/7

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：



代码：

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

while True:
    try:
        s=input()
    except EOFError:
        break
    if ord(s[0])>=ord('A'):
        ans=''
        for i in range(len(s)):
            temp=''
            pos=huffman_tree
            while True:
                if s[i] in pos.left.alphabet:
                    temp+='0'
                    if not pos.left.left:
                        break
                    else:
                        pos=pos.left
                elif s[i] in pos.right.alphabet:
                    temp+='1'
                    if not pos.right.left:
                        break
                    else:
                        pos=pos.right
                else:
                    break
            ans+=temp
        print(ans)
    else:
        ans=''
        i=0
        s+='2'
        pos=huffman_tree
        while i<len(s):
            if s=='2':
                temp = list(pos.alphabet)
                ans += temp[0]
                break
            elif s[i]=='0':
                if pos.left:
                    pos=pos.left
                    i+=1
                else:
                    temp=list(pos.alphabet)
                    ans+=temp[0]
                    pos=huffman_tree

            else:
                if pos.right:
                    pos=pos.right
                    i+=1
                else:
                    temp = list(pos.alphabet)
                    ans += temp[0]
                    pos = huffman_tree
        print(ans)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250420103307.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本周还要忙于数理方法和统计方法的考试，因此手搓heap的题目就先放了放，周四之后期中正式结束再说吧（叹气）









