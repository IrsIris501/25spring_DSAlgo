# Assignment #5: 链表、栈、队列和归并排序

Updated 1515 GMT+8 Mar 24, 2025

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

### LC21.合并两个有序链表

linked list, https://leetcode.cn/problems/merge-two-sorted-lists/

思路：



代码：

```python
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        def reverse(head: ListNode):
            prev=None
            while head:
                next_node=head.next
                head.next=prev
                prev=head
                head=next_node
            return prev
        list1=reverse(list1)
        list2=reverse(list2)
        print('reversed')
        ans=None
        while list1 and list2:
            if list1.val>list2.val:
                ans=ListNode(list1.val, ans)
                list1=list1.next
            else:
                ans=ListNode(list2.val, ans)
                list2=list2.next
        while list1:
            ans=ListNode(list1.val, ans)
            list1=list1.next
        while list2:
            ans=ListNode(list2.val, ans)
            list2-list2.next
        print('returned')
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250320190140.png)



### LC234.回文链表

linked list, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现。</mark>



代码：

```python
class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: bool
            """

            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next




            prev=None
            while slow:
                next_node=slow.next
                slow.next=prev
                prev=slow
                slow=next_node

            cur1=head
            cur2=prev

            while cur1.next!=None:
                if cur1.val!=cur2.val:
                    return False
                cur1=cur1.next
                cur2=cur2.next
            return True

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250320190323.png)



### LC1472.设计浏览器历史记录

doubly-lined list, https://leetcode.cn/problems/design-browser-history/

<mark>请用双链表实现。</mark>



代码：

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleListNode:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def print_list(self):
        pointer=self.head
        while pointer:
            print(pointer.val, end=' ')
            pointer=pointer.next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.items=DoubleListNode()
        self.items.append(homepage)
        self.pointer=self.items.head

    def visit(self, url: str) -> None:
        self.pointer.next=Node(url)
        tmp=self.pointer
        self.pointer=self.pointer.next
        self.pointer.prev=tmp

    def back(self, steps: int) -> str:
        count=steps
        while self.pointer.prev and count:
            self.pointer=self.pointer.prev
            count-=1
        return self.pointer.val

    def forward(self, steps: int) -> str:
        count=steps
        while self.pointer.next and count:
            self.pointer=self.pointer.next
            count-=1
        return self.pointer.val
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250324141350.png)



### 24591: 中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：



代码：

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

n=int(input())
for _ in range(n):
    s=input()
    print(*suffixize(s))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250324125713.png)



### 03253: 约瑟夫问题No.2

queue, http://cs101.openjudge.cn/practice/03253/

<mark>请用队列实现。</mark>



代码：

```python
from collections import deque

while True:
    n, p, m=map(int, input().split())
    if n==p==m==0:
        break
    q=deque()
    for i in range(1, n+1):
        q.append(i)
    for i in range(p-1):
        q.append(q.popleft())
    count=0
    exit_list=[]
    while q:
        tmp=q.popleft()
        count+=1
        if count!=m:
            q.append(tmp)
        else:
            exit_list.append(tmp)
            count=0
    print(*exit_list, sep=',')




```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20250324130836230](C:\Users\Eric_\AppData\Roaming\Typora\typora-user-images\image-20250324130836230.png)



### 20018: 蚂蚁王国的越野跑

merge sort, http://cs101.openjudge.cn/practice/20018/

思路：



代码：

```python
# pylint: skip-file
def merge_sort(arr):
    global count
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                count+=len(left)-i
                arr[k]=right[j]
                j+=1
                k+=1
            else:
                arr[k]=left[i]
                i+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

n=int(input())
velocity=[]
count=0
for i in range(n):
    velocity.append(int(input()))
velocity.reverse()
merge_sort(velocity)
print(count)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250324151354.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉最近比较摆，线性结构部分因为寒假学过了所以还能应付，树的部分寒假的时候就没看懂，感觉相当抽象









