# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build(pre: deque):
    if not pre:
        return None
    val = pre.popleft()
    if val == '.':
        return None
    node = TreeNode(val)
    node.left = build(pre)
    node.right = build(pre)
    return node

def inorder(root):
    global ans_in
    if root.left:
        inorder(root.left)
    ans_in += root.val
    if root.right:
        inorder(root.right)

def postorder(root):
    global ans_post
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    ans_post += root.val

s = deque(input())
root = build(s)
ans_in = ''
ans_post = ''
inorder(root)
postorder(root)
print(ans_in)
print(ans_post)
