# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, s, num):
        self.val=s
        self.children=[]
        self.num=num

def build_tree(stack):
    q=deque()
    item, count=stack.popleft()
    tree=TreeNode(item, count)
    q.append(tree)
    while stack and q:
        current_tree=q.popleft()
        for i in range(current_tree.num):
            item, count=stack.popleft()
            child=TreeNode(item, count)
            current_tree.children.append(child)
            q.append(child)
    return tree

def post_order(tree: TreeNode):
    global ans
    for i in tree.children:
        post_order(i)
    ans.append(tree.val)

t=int(input())
ans=[]
for i in range(t):
    stack=deque()
    temp_stack=input().split()
    for j in range(len(temp_stack)):
        if ord('A')<=ord(temp_stack[j])<=ord('Z'):
            temp = temp_stack[j]
        else:
            stack.append((temp, int(temp_stack[j])))
    tree=build_tree(stack)
    post_order(tree)
print(*ans)


