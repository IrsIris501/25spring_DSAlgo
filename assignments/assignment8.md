# Assignment #8: 树为主

Updated 1529 GMT+8 Apr 15, 2025

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

### LC108.将有序数组转换为二叉树

dfs, https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

思路：并不会建树，参考了题解



代码：

```python
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def helper(left, right) -> TreeNode:
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=helper(left, mid-1)
            root.right=helper(mid+1, right)
            return root

        return helper(0, len(nums)-1)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250414102349.png)



### M27928:遍历树

 adjacency list, dfs, http://cs101.openjudge.cn/practice/27928/

思路：



代码：

```python
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.child=[]


n=int(input())
node_dict=dict()
all_node=set()
children_node=set()
for i in range(n):
    l=list(map(int, input().split()))
    node_dict[l[0]]=l[1::]
    all_node.add(l[0])
    children_node.update(l[1::])
    if i==0:
        root_val=l[0]

root_val=(all_node-children_node).pop()
def build_tree(root_val):
    root=TreeNode(root_val)
    for i in node_dict[root_val]:
        root.child.append(build_tree(i))
    return root

tree=build_tree(root_val)
traversal_list=[]
def traverse(tree: TreeNode, last=None):
    if not tree.child:
        traversal_list.append(tree.val)
        return
    if tree==last:
        traversal_list.append(tree.val)
        return
    temp=tree.child+[tree]
    temp.sort(key=lambda x: x.val)
    for i in range(len(temp)):
        traverse(temp[i], tree)

traverse(tree)
print(*traversal_list, sep='\n')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250414124807.png)



### LC129.求根节点到叶节点数字之和

dfs, https://leetcode.cn/problems/sum-root-to-leaf-numbers/

思路：



代码：

```python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        global count
        count=0
        def dfs(start: TreeNode, num: str):
            global count
            if not start.left and not start.right:
                count+=int(num)
                return
            if start.left!=None:
                dfs(start.left, num+str(start.left.val))
            if start.right!=None:
                dfs(start.right, num+str(start.right.val))
            return
        dfs(root, str(root.val))
        return count
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250414101151.png)



### M22158:根据二叉树前中序序列建树

tree, http://cs101.openjudge.cn/practice/22158/

思路：



代码：

```python
# pylint: skip-file
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(pre, mid):
    if len(pre)==1:
        return TreeNode(pre[0])
    if not pre:
        return None
    for i in range(len(mid)):
        if mid[i]==pre[0]:
            break
    return TreeNode(pre[0], left=build_tree(pre[1:i+1], mid[0:i]), right=build_tree(pre[i+1:], mid[i+1:]))

def post(tree):
    global ans
    if tree.left:
        post(tree.left)
    if tree.right:
        post(tree.right)
    ans+=tree.val

while True:
    try:
        pre=list(input())
        mid=list(input())
    except:
        break
    tree=build_tree(pre, mid)
    ans=''
    post(tree)
    print(ans)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250414131150.png)



### M24729:括号嵌套树

dfs, stack, http://cs101.openjudge.cn/practice/24729/

思路：



代码：

```python
# pylint: skip-file
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.child=[]

s=list(input())
stack=[]
for i in range(len(s)):
    if s[i]==')':
        temp=[]
        while True:
            t=stack.pop()
            if t=='(':
                break
            temp.append(t)
        pos=stack.pop()
        temp.reverse()
        pos.child+=temp
        stack.append(pos)
    elif s[i]==',':
        continue
    elif s[i]=='(':
        stack.append(s[i])
    else:
        stack.append(TreeNode(s[i]))

root=stack.pop()

def pre(tree):
    global pre_str
    pre_str+=tree.val
    for i in tree.child:
        pre(i)

def post(tree):
    global post_str
    for i in tree.child:
        post(i)
    post_str+=tree.val

pre_str=''
post_str=''
pre(root)
post(root)
print(pre_str)
print(post_str)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250414194530.png)



### LC3510.移除最小数对使数组有序II

doubly-linked list + heap, https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉很多树的题目，建树这一步最难，虽然一般都是递归/类似递归









