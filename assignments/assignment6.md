# Assignment #6: 回溯、树、双向链表和哈希表

Updated 1513 GMT+8 Mar 31, 2025

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

### LC46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路：



代码：

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        vis=set()
        def backtrack(first: int, output: list[int]):
            if first==n:
                ans.append(output)
                return
            for i in range(n):
                if nums[i] not in vis:
                    vis.add(nums[i])
                    backtrack(first+1, output+[nums[i]])
                    vis.remove(nums[i])
        backtrack(0, [])

        return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250331103016.png)



### LC79: 单词搜索

backtracking, https://leetcode.cn/problems/word-search/

思路：



代码：

```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        global avail
        avail=False
        def dfs(x, y, i: int):
            global avail

            if i==l:
                avail=True
                return
            for j in range(4):
                nx=x+dx[j]
                ny=y+dy[j]
                if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and board[nx][ny]==word[i]:
                    visited.add((nx, ny))
                    dfs(nx, ny, i+1)
                    visited.remove((nx, ny))

        dx=[1, -1, 0, 0]
        dy=[0, 0, 1, -1]
        n=len(board)
        m=len(board[0])
        l=len(word)
        for j in range(n):
            for k in range(m):
                if board[j][k]==word[0]:
                    visited=set()
                    visited.add((j, k))
                    dfs(j, k, 1)
                    if avail:
                        return True
        return False
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250331110311.png)



### LC94.二叉树的中序遍历

dfs, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：



代码：

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        global ans
        ans=[]
        def in_order_trav(root):
            global ans
            if root:
                in_order_trav(root.left)
                ans.append(root.val)
                in_order_trav(root.right)
        in_order_trav(root)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250331114645.png)



### LC102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：



代码：

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ans=[]
        q=deque()
        q.append((root, 0))
        cur_lev=-1
        while q:
            head, level=q.popleft()
            if head:
                if cur_lev!=level:
                    cur_lev+=1
                    ans.append([])
                ans[-1].append(head.val)
                q.append((head.left, level+1))
                q.append((head.right, level+1))
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250331134436.png)



### LC131.分割回文串

dp, backtracking, https://leetcode.cn/problems/palindrome-partitioning/

思路：



代码：

```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        palindrome=[[False for j in range(n)] for i in range(n)]
        global ans
        ans=[]

        for i in range(n):
            palindrome[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                palindrome[i][i+1]=True
        for j in range(n):
            for i in range(j-1):
                if s[i]==s[j]:
                    palindrome[i][j]=palindrome[i+1][j-1]
        def dfs(i, route: list[str]):
            global ans
            if i==n:
                ans.append(route)
                return
            for j in range(i+1, n+1):
                if palindrome[i][j-1]:
                    dfs(j, route+[s[i:j]])

        dfs(0, [])
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250331150350.png)



### LC146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/1.jpg)

在家园三楼肠粉窗口发现一个deque队列，有人点了一份肠粉就会append，做好了一份就popleft









