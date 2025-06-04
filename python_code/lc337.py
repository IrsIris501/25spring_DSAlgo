# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0, 0
            left1, left2 = dfs(node.left)
            right1, right2 = dfs(node.right)
            return left2 + right2 + node.val, max(left1, left2) + max(right1, right2)
        a, b = dfs(root)
        return max(a, b)

