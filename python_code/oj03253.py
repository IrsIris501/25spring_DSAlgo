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



