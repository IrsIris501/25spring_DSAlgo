from collections import deque, defaultdict



n=int(input())
words=[]
for i in range(n):
    words.append(input())
start, end=input().split()

pattern_map=defaultdict(list)
for word in words:
    for i in range(4):
        pattern=word[:i]+'*'+word[i+1:]
        pattern_map[pattern].append(word)


q=deque()
q.append(start)
prev={start: None}
visited=set([start])
can_reach=False
while q:
    cur=q.popleft()
    if cur==end:
        path=[]
        while prev[cur]:
            path.append(cur)
            cur=prev[cur]
        path.append(start)
        path.reverse()
        print(*path)
        can_reach=True
        break
    for i in range(4):
        pattern=cur[:i]+'*'+cur[i+1:]
        for next in pattern_map[pattern]:
            if next==cur:
                continue
            else:
                if next not in visited:
                    q.append(next)
                    visited.add(next)
                    prev[next]=cur


if not can_reach:
    print('NO')

