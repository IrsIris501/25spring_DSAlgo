# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append((root, 1))
        cur_level=0
        while q:
            pos, level=q.popleft()
            if level>cur_level:
                cur_level=level
                ans.append([])
            ans[-1].append(pos.val)
            if pos.left:
                q.append((pos.left, level+1))
            if pos.right:
                q.append((pos.right, level+1))
        for i in range(len(ans)):
            if i%2:
                ans[i].reverse()
        return ans

