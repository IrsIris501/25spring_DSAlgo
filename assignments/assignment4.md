# Assignment #4: 位操作、栈、链表、堆和NN

Updated 1033 UTC+8, Mar 13, 2025

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

### 136.只出现一次的数字

bit manipulation, https://leetcode.cn/problems/single-number/



<mark>请用位操作来实现，并且只使用常量额外空间。</mark>



代码：

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp=nums[0]
        for i in range(1, len(nums)):
            temp^=nums[i]
        return temp

nums=list(map(int, input().split()))
s=Solution()
print(s.singleNumber(nums))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250311155847.png)



### 20140:今日化学论文

stack, http://cs101.openjudge.cn/practice/20140/



思路：



代码：

```python
s=input()
stack=[]
ans=''
i=0
while i<len(s):
    if ord('0')<=ord(s[i])<=ord('9'):
        j=i
        while ord('0')<=ord(s[j])<=ord('9'):
            j+=1
        stack.append(int(s[i:j]))
        i=j
    elif ord('a')<=ord(s[i])<=ord('z'):
        stack.append(s[i])
        i+=1
    elif s[i]==']':
        i+=1
        temp=''
        while stack and isinstance(stack[-1], str):
            temp=stack.pop()+temp
        if stack:
            temp=temp*stack.pop()
            stack.append(temp)
    else:
        i+=1
for j in stack:
    ans+=j
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250311164722.png)



### 160.相交链表

linked list, https://leetcode.cn/problems/intersection-of-two-linked-lists/



思路：



代码：

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        def list_node_len(head: ListNode) -> int:
            pointer=head
            ans=0
            while pointer:
                pointer=pointer.next
                ans+=1
            return ans
        len_a=list_node_len(headA)
        len_b=list_node_len(headB)
        pointer_a=headA
        pointer_b=headB
        if len_a>len_b:
            for i in range(len_a-len_b):
                pointer_a=pointer_a.next
        else:
            for i in range(len_b-len_a):
                pointer_b=pointer_b.next
        while pointer_b:
            if pointer_b==pointer_a:
                return pointer_b
            pointer_b=pointer_b.next
            pointer_a=pointer_a.next
        return None
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250312144809.png)



### 206.反转链表

linked list, https://leetcode.cn/problems/reverse-linked-list/



思路：



代码：

```python
# I'm using Python(not Python 3) in mistake at that moment.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        current=head

        while current!=None:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        return prev
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250312145053.png)



### 3478.选出和最大的K个元素

heap, https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/



思路：heapq要使用增量的方法push，不能每次都重新搞一个。这就需要使用三元数组，并按照nums1[i]排序，且每次push之后如果超过k个就pop，并且要注意的是一旦被heappop的元素之后就再也不可能被push，因此pop之后就可以不管（因为它太小了）。另外，用变量s表示heap的和，不用每次都sum(heap)，sum()是O(N)的



代码：

```python
class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        import heapq
        answer=[0 for i in range(len(nums1))]
        temp=[]
        for i in range(len(nums1)):
            temp.append((nums1[i], nums2[i], i))
        temp.sort(key=lambda x:x[0])
        heap=[]
        s=0
        pointer=0
        for i in range(len(nums1)):
            while pointer<i:
                if temp[pointer][0]<temp[i][0]:
                    heapq.heappush(heap, temp[pointer][1])
                    s+=temp[pointer][1]
                    pointer+=1
                    if len(heap)>k:
                        s-=heapq.heappop(heap)
                else:
                    break
            answer[temp[i][2]]=s
        return answer
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250313102810.png)



### Q6.交互可视化neural network

https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises

**Your task:** configure a neural network that can separate the orange dots from the blue dots in the diagram, achieving a loss of less than 0.2 on both the training and test data.

**Instructions:**

In the interactive widget:

1. Modify the neural network hyperparameters by experimenting with some of the following config settings:
   - Add or remove hidden layers by clicking the **+** and **-** buttons to the left of the **HIDDEN LAYERS** heading in the network diagram.
   - Add or remove neurons from a hidden layer by clicking the **+** and **-** buttons above a hidden-layer column.
   - Change the learning rate by choosing a new value from the **Learning rate** drop-down above the diagram.
   - Change the activation function by choosing a new value from the **Activation** drop-down above the diagram.
2. Click the Play button above the diagram to train the neural network model using the specified parameters.
3. Observe the visualization of the model fitting the data as training progresses, as well as the **Test loss** and **Training loss** values in the **Output** section.
4. If the model does not achieve loss below 0.2 on the test and training data, click reset, and repeat steps 1–3 with a different set of configuration settings. Repeat this process until you achieve the preferred results.

给出满足约束条件的<mark>截图</mark>，并说明学习到的概念和原理。





## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

吃晚饭的时候突然想到了用三元数组排序的方法，看来脑子切换一下确实是非常有用的！









