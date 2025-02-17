from collections import deque
def joseph_problem(n, m):
    queue=deque([i for i in range(1, n+1)])
    while len(queue)>1:
        for i in range(m-1):
            queue.append(queue.popleft())
        queue.popleft()
    return queue.pop()

while True:
    n, m=map(int, input().split())
    if (n, m)==(0, 0):
        break
    print(joseph_problem(n, m))