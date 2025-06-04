# pylint: skip-file
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(mid, post):
    if len(post) == 1:
        return TreeNode(post[0])
    if not post:
        return None
    for i in range(len(mid)):
        if mid[i] == post[-1]:
            break
    return TreeNode(post[-1], left = build_tree(mid[0:i], post[0:i]), right = build_tree(mid[i+1:], post[i:-1]))

def pre(root):
    global ans
    ans += root.val
    if root.left:
        pre(root.left)
    if root.right:
        pre(root.right)

ans = ''
mid = input()
post = input()
root = build_tree(mid, post)
pre(root)
print(ans)