# pylint: skip-file
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(pre, mid):
    if len(pre)==1:
        return TreeNode(pre[0])
    if not pre:
        return None
    for i in range(len(mid)):
        if mid[i]==pre[0]:
            break
    return TreeNode(pre[0], left=build_tree(pre[1:i+1], mid[0:i]), right=build_tree(pre[i+1:], mid[i+1:]))

def post(tree):
    global ans
    if tree.left:
        post(tree.left)
    if tree.right:
        post(tree.right)
    ans+=tree.val

while True:
    try:
        pre=list(input())
        mid=list(input())
    except:
        break
    tree=build_tree(pre, mid)
    ans=''
    post(tree)
    print(ans)

