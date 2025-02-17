from collections import deque
t=int(input())
for _ in range(t):
    q=deque()

    n=int(input())
    for i in range(n):
        type, c=map(int, input().split())
        if type==1:
            q.append(c)
        elif type==2:
            if c:
                q.pop()
            else:
                q.popleft()
    if q:
        print(*q)
    else:
        print('NULL')
