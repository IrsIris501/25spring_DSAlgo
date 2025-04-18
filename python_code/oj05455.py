from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

nums=list(map(int, input().split()))
in_tree_set=set()
bst=TreeNode(nums[0])
in_tree_set.add(nums[0])
for i in range(1, len(nums)):
    if nums[i] in in_tree_set:
        continue

    pos=bst
    while True:
        if nums[i]>pos.val:
            if pos.right:
                pos=pos.right
            else:
                pos.right=TreeNode(nums[i])
                break
        else:
            if pos.left:
                pos=pos.left
            else:
                pos.left=TreeNode(nums[i])
                break
    in_tree_set.add(nums[i])

q=deque()
q.append(bst)
ans=[]
while q:
    pos=q.popleft()
    ans.append(pos.val)
    if pos.left:
        q.append(pos.left)
    if pos.right:
        q.append(pos.right)
print(*ans)