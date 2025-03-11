# Assignment #3: 惊蛰 Mock Exam

Updated 1537 UTC+8, 11 Mar, 2025

2025 spring, Complied by <mark>物理学院 陈虹骏</mark>



> **说明：**
>
> 1. **惊蛰⽉考**：<mark>AC4</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：



代码：

```python
def avail(s):
    s=list(s)
    flag=0
    for i in s:
        if i=='@':
            flag+=1
    if flag!=1:
        return False
    if s[0]=='.' or s[0]=='@' or s[-1]=='@' or s[-1]=='.':
        return False
    flag2=0
    flag3=0
    for i in range(len(s)):
        if s[i]=='@':
            if s[i-1]=='.':
                return False
            flag2=1
        if s[i]=='.':
            if s[i-1]=='@':
                return False
            elif flag2:
                flag3+=1
    if not flag3:
        return False
    return True
while True:
    try:
        s=input()
    except:
        break
    print('YES' if avail(s) else 'NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250306150018.png)



### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：



代码：

```python
n=int(input())
s=input()
matrix=[['' for i in range(n)] for j in range(len(s)//n)]
s=list(s)
x=0
y=0
heading=1
for i in range(len(s)):
    matrix[x][y]=s[i]
    if (y==n-1 and heading==1) or (y==0 and heading==-1):
        x+=1
        heading=-heading
    else:
        y+=heading
ans=''
for i in range(n):
    for j in range(len(s)//n):
        ans+=matrix[j][i]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250306150100.png)



### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：



代码：

```python
while True:
    players=set()
    n, m=map(int, input().split())
    if (n, m)==(0, 0):
        break
    stat=dict()
    for i in range(n):
        num_list=list(map(int, input().split()))
        for j in num_list:
            if j in players:
                stat[j]+=1
            else:
                players.add(j)
                stat[j]=1
    players_list=list(players)
    point=[]
    for i in players_list:
        point.append((i, stat[i]))
    point.sort(reverse=True, key=lambda x:x[1])
    i=0
    flag=0
    ans=[]
    while i<len(point):
        if flag and point[i][1]<point[i-1][1]:
            break
        if not flag and point[i][1]<point[i-1][1]:
            flag=1
        if flag:
            ans.append(point[i][0])
        i+=1
    ans.sort()
    print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250306150140.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：



代码：

```python
d=int(input())
n=int(input())
x=[]
y=[]
t=[]
for i in range(n):
    a, b, c=map(int, input().split())
    x.append(a)
    y.append(b)
    t.append(c)
ans=0
cnt=0
for i in range(1025):
    for j in range(1025):
        temp=0
        for k in range(n):
            if abs(x[k]-i)<=d and abs(y[k]-j)<=d:
                temp+=t[k]
        if temp>ans:
            ans=temp
            cnt=1
        elif temp==ans:
            cnt+=1
print(cnt, ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250306150210.png)



### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：要注意dx和dy的顺序使得字典序最小



代码：

```python
# pylint: skip-file
dx=[-1, 1, -2, 2, -2, 2, -1, 1]
dy=[-2, -2, -1, -1, 1, 1, 2, 2]
def avail(x, y, p, q, visited):
    return 0<=x<p and 0<=y<q and not visited[x][y]

def dfs(x: int, y: int, path:str, p, q):
    global visited
    global can_reach
    if can_reach:
        return
    path+=chr(y+65)+str(x+1)
    full=True
    for i in range(p):
        if False in visited[i]:
            full=False
            break
    if full:
        can_reach=True
        print(path)
        return
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if avail(nx, ny, p, q, visited):
            visited[nx][ny]=True
            dfs(nx, ny, path, p, q)
            visited[nx][ny]=False




n=int(input())
for _ in range(n):
    p, q=map(int, input().split())
    print('Scenario #'+str(_+1)+':')

    can_reach=False
    for i in range(p):
        for j in range(q):
            visited = [[False for x in range(q)] for y in range(p)]
            visited[i][j] = True
            dfs(i, j, '', p, q)
            if can_reach:
                break
        if can_reach:
            break
    if not can_reach:
        print('impossible')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250310142311.png)



### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：



代码：

```python
import heapq

t=int(input())
for _ in range(t):
    m, n=map(int, input().split())
    sums=list(map(int, input().split()))
    heapq.heapify(sums)
    for i in range(m-1):
        b=sorted(list(map(int, input().split())))
        heap = []
        visited = set()
        # Push the initial sum of the first elements
        for j in range(n):
            heapq.heappush(heap, (sums[j] + b[0], j, 0))
            visited.add((j, 0))
        sums_temp = []

        while heap and len(sums_temp) < n:
            sum_val, i_sum, i_b = heapq.heappop(heap)
            sums_temp.append(sum_val)
            # Move right in b (without moving down in sums!)
            if i_b + 1 < len(b):
                if (i_sum, i_b + 1) not in visited:
                    new_sum = sums[i_sum] + b[i_b + 1]
                    heapq.heappush(heap, (new_sum, i_sum, i_b + 1))
                    visited.add((i_sum, i_b + 1))
            if i_sum + 1 < len(sums):
                if (i_sum + 1, i_b) not in visited:
                    new_sum = sums[i_sum + 1] + b[i_b]
                    heapq.heappush(heap, (new_sum, i_sum + 1, i_b))
                    visited.add((i_sum + 1, i_b))
                    # Update sums for next iteration
        heapq.heapify(sums_temp)
        sums = sums_temp
    sums.sort()
    print(*sums)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/IrsIris501/img/main/20250310173610.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉上学期的dfs就不是很学明白，这下第5题就坏了

第6题在自己做TLE，询问deepseek就WA之后参考了题解，发现需要初始化heap的时候要把sums中每一个都加上b[0]

顺带一提，发现一个Edge的插件叫Sider还挺方便的，也很快，deepseek-r1:70b 每天最多可以用25次 free，还有一些别的模型







