# Assignment #1: 虚拟机，Shell & 大模型

Updated 1154 UTC+8, Mar 3, 2025

2025 spring, Complied by <mark>陈虹骏 物理学院</mark>



> 作业的各项评分细则及对应的得分情况
>
> | 标准                                 | 等级                                                         | 得分 |
> | ------------------------------------ | ------------------------------------------------------------ | ---- |
> | 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
> | 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>没有提供源码：0分 | 1 分 |
> | AC代码截图                           | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
> | 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
> | 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
> | 总得分： 5                           | 总分满分：5分                                                |      |
>
> 
>
> **说明：**
>
> 1. **解题与记录：**
>    
>    - 对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **课程平台与提交安排：**
>
>    - 我们的课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在第2周选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>    
>    - 提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**
>
>    - 如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：



代码：

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
    def prt(self):
        print('{}/{}'.format(self.numerator, self.denominator))
import math
def add(frac1, frac2):
    numerator1=frac1.numerator
    numerator2=frac2.numerator
    denominator1=frac1.denominator
    denominator2=frac2.denominator
    numerator1 *= denominator2 // math.gcd(denominator1, denominator2)
    numerator2 *= denominator1 // math.gcd(denominator1, denominator2)
    num3=numerator2+numerator1
    den3=denominator1*denominator2//math.gcd(denominator1, denominator2)
    num3 = num3 // math.gcd(num3, den3)
    den3 = den3 // math.gcd(num3, den3)
    frac3=Fraction(num3, den3)
    return frac3

a, b, c, d=map(int, input().split())
frac1=Fraction(a, b)
frac2=Fraction(c, d)
add(frac1, frac2).prt()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-02-22%20125103.png)



### 1760.袋子里最少数目的球

 https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/




思路：



代码：

```python
# 已经更改为本地运行的形式
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        import math
        right=max(nums)
        left=0
        while True:
            current=int(math.ceil((right+left)/2))
            operations=0
            for i in nums:
                operations+=math.ceil(i/current)-1
            if operations>maxOperations:
                left=current
            elif operations<=maxOperations:
                right=current
            if right-left==1:
                return right
            if current==1:
                return 1

nums=list(map(int, input().split()))
maxOperations=int(input())
s=Solution()
print(s.minimumSize(nums, maxOperations))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-02-22%20140721.png)



### 04135: 月度开销

http://cs101.openjudge.cn/practice/04135



思路：



代码：

```python
import math
def min_cost(n, m, cost):
    left=max(cost)-1
    right=sum(cost)
    while True:
        current=math.ceil((right+left)/2)
        temp=0
        months=1
        for i in cost:
            if temp+i<=current:
                temp+=i
            else:
                temp=i
                months+=1
        if months>m:
            left=current
        elif months<=m:
            right=current

        if right-left==1:
            return right


n, m=map(int, input().split())
cost=[]
for i in range(n):
    cost.append(int(input()))
print(min_cost(n, m, cost))


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-02-22%20142025.png)



### 27300: 模型整理

http://cs101.openjudge.cn/practice/27300/



思路：



代码：

```python
n=int(input())
model_list=[]
def value(x):
    if x[-1]=='B':
        return float(x[:-1:])*1000
    else:
        return float(x[:-1:])

for _ in range(n):
    flag=False
    model_name, para=input().split('-')
    for i in range(len(model_list)):
        if model_list[i][0]==model_name:
            model_list[i][1].append(para)
            flag=True
            break
    if not flag:
        model_list.append((model_name, [para]))

model_list.sort(key=lambda x:x[0])
for i in range(len(model_list)):
    print(model_list[i][0]+': ', end='')
    print(*sorted(model_list[i][1], key=lambda x:value(x)), sep=', ')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-02-22%20144621.png)



### Q5. 大语言模型（LLM）部署与测试

本任务旨在本地环境或通过云虚拟机（如 https://clab.pku.edu.cn/ 提供的资源）部署大语言模型（LLM）并进行测试。用户界面方面，可以选择使用图形界面工具如 https://lmstudio.ai 或命令行界面如 https://www.ollama.com 来完成部署工作。

测试内容包括选择若干编程题目，确保这些题目能够在所部署的LLM上得到正确解答，并通过所有相关的测试用例（即状态为Accepted）。选题应来源于在线判题平台，例如 OpenJudge、Codeforces、LeetCode 或洛谷等，同时需注意避免与已找到的AI接受题目重复。已有的AI接受题目列表可参考以下链接：
https://github.com/GMyhf/2025spring-cs201/blob/main/AI_accepted_locally.md

请提供你的最新进展情况，包括任何关键步骤的截图以及遇到的问题和解决方案。这将有助于全面了解项目的推进状态，并为进一步的工作提供参考。



使用的是ollama deepseek-r1:8b，但是这个模型对本次作业第一题（leetcode: Medium）的思考时间就极长，十多分钟还没有给出答案，并且之前还给过一道比较简单的数学题

```
sin x = 0.25 + 0.75i, 求复数x
```

也思考了很长时间还没给出答案，感觉8b的模型还是不大聪明，但是运行的时候风扇动静已经比较大（至少比我玩Euro Truck Simulator 2的时候大），且CPU利用率高达50%

想着是不是8b太小了，于是下载了32b，但是32b运行的时候生成文字的速度极其慢，一秒钟出不来几个字，并且CPU利用率也只有50%，但是32G的内存几乎用满了，无能为力



云端虚拟机卡在了安装ollama上，因为挂不了vpn





### Q6. 阅读《Build a Large Language Model (From Scratch)》第一章

作者：Sebastian Raschka

请整理你的学习笔记。这应该包括但不限于对第一章核心概念的理解、重要术语的解释、你认为特别有趣或具有挑战性的内容，以及任何你可能有的疑问或反思。通过这种方式，不仅能巩固你自己的学习成果，也能帮助他人更好地理解这一部分内容。





## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

寒假啥也没干，目前已经学会了线性结构，做完了pre-problem list中线性结构的题目



