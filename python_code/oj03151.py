from collections import deque
def pots(a, b, c):
    global source
    q=deque()
    q.append((0, 0))
    inq=set()
    inq.add((0, 0))

    while q:
        a_now, b_now=q.popleft()
        if a_now==c:
            return 1
        elif b_now==c:
            return 2

        # FILL(1)
        if a_now!=a:
            if (a, b_now) not in inq:
                q.append((a, b_now))
                inq.add((a, b_now))
                source[a][b_now]=[a_now, b_now, 'FILL(1)']

        # FILL(2)
        if b_now!=b:
            if (a_now, b) not in inq:
                q.append((a_now, b))
                inq.add((a_now, b))
                source[a_now][b]=[a_now, b_now, 'FILL(2)']

        # DROP(1)
        if a_now:
            if (0, b_now) not in inq:
                q.append((0, b_now))
                inq.add((0, b_now))
                source[0][b_now]=[a_now, b_now, 'DROP(1)']

        # DROP(2)
        if b_now:
            if (a_now, 0) not in inq:
                q.append((a_now, 0))
                inq.add((a_now, 0))
                source[a_now][0]=[a_now, b_now, 'DROP(2)']

        # POUR(1, 2)
        if (max(0, a_now-b+b_now), min(b, b_now+a_now)) not in inq:
            q.append((max(0, a_now-b+b_now), min(b, b_now+a_now)))
            inq.add((max(0, a_now-b+b_now), min(b, b_now+a_now)))
            source[max(0, a_now-b+b_now)][min(b, b_now+a_now)]=[a_now, b_now, 'POUR(1,2)']

        # POUR(2, 1)
        if (min(a, a_now+b_now), max(0, a_now+b_now-a)) not in inq:
            q.append((min(a, a_now+b_now), max(0, a_now+b_now-a)))
            inq.add((min(a, a_now+b_now), max(0, a_now+b_now-a)))
            source[min(a, a_now+b_now)][max(0, a_now+b_now-a)]=[a_now, b_now, 'POUR(2,1)']
    return 0

a, b, c=map(int, input().split())
opstack=[]
source=[[[] for i in range(b+1)] for j in range(a+1)]
out=pots(a, b, c)
if out==1:
    for i in range(b+1):
        if source[c][i]:
            cur2=i
            break
    cur1=c
    while (cur1, cur2)!=(0, 0):
        opstack.append(source[cur1][cur2][2])
        cur1, cur2=source[cur1][cur2][0], source[cur1][cur2][1]
    print(len(opstack))
    while opstack:
        print(opstack.pop())
elif out==2:
    for i in range(a+1):
        if source[i][c]:
            cur1=i
            break
    cur2=c
    while (cur1, cur2)!=(0, 0):
        opstack.append(source[cur1][cur2][2])
        cur1, cur2=source[cur1][cur2][0], source[cur1][cur2][1]
    print(len(opstack))
    while opstack:
        print(opstack.pop())
elif not out:
    print('impossible')



