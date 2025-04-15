# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ans=[]
        q=deque()
        q.append((root, 0))
        cur_lev=-1
        while q:
            head, level=q.popleft()
            if head:
                if cur_lev!=level:
                    cur_lev+=1
                    ans.append([])
                ans[-1].append(head.val)
                q.append((head.left, level+1))
                q.append((head.right, level+1))
        return ans

