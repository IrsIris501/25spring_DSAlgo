# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        global count
        count=0
        def dfs(start: TreeNode, num: str):
            global count
            if not start.left and not start.right:
                count+=int(num)
                return
            if start.left!=None:
                dfs(start.left, num+str(start.left.val))
            if start.right!=None:
                dfs(start.right, num+str(start.right.val))
            return
        dfs(root, str(root.val))
        return count

