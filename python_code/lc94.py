# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        global ans
        ans=[]
        def in_order_trav(root):
            global ans
            if root:
                in_order_trav(root.left)
                ans.append(root.val)
                in_order_trav(root.right)
        in_order_trav(root)
        return ans


s=Solution()
s.inorderTraversal()