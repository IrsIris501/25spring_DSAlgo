import heapq
from collections import deque


class TreeNode:
    def __init__(self, val, count=0, left=None, right=None):
        self.val=val
        self.count=count
        self.left=left
        self.right=right
    def __lt__(self, other):
        return self.val<other.val

n=int(input())
weight=list(map(int, input().split()))
heap=[]
for i in range(len(weight)):
    heap.append(TreeNode(weight[i], count=1))
heapq.heapify(heap)
while len(heap)>1:
    t1=heapq.heappop(heap)
    t2=heapq.heappop(heap)
    temp=TreeNode(t1.val+t2.val, count=0, left=t1, right=t2)
    heapq.heappush(heap, temp)
huffman_tree=heapq.heappop(heap)
q=deque()
q.append((huffman_tree, 0))
ans=0
while q:
    pos, layer=q.popleft()
    if pos.count:
        ans+=pos.val*layer
    if pos.left:
        q.append((pos.left, layer+1))
    if pos.right:
        q.append((pos.right, layer+1))
print(ans)
