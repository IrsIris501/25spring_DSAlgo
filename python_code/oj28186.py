from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
q = deque()
for i in range(n):
    q.append((i+1, a[i]))
while len(q) > 1:
    seq, num = q.popleft()
    if num - m > 0:
        q.append((seq, num - m))
print(q[0][0])

