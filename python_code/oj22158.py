# pylint: skip-file
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(pre, mid):
    if len(pre) == 1:
        return TreeNode(pre[0])
    if not pre:
        return None
    for i in range(len(mid)):
        if pre[0] == mid[i]:
            break
    return TreeNode(pre[0], left = build_tree(pre[1:i+1], mid[0:i]), right = build_tree(pre[i+1:], mid[i+1:]))

def post(root):
    global ans
    if root.left:
        post(root.left)
    if root.right:
        post(root.right)
    ans += root.val
while True:
    try:
        pre = list(input())
    except EOFError:
        break
    mid = list(input())
    ans = ''
    root = build_tree(pre, mid)
    post(root)
    print(ans)

