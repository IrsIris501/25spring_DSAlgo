# pylint: skip-file
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.child=[]

s=list(input())
stack=[]
for i in range(len(s)):
    if s[i]==')':
        temp=[]
        while True:
            t=stack.pop()
            if t=='(':
                break
            temp.append(t)
        pos=stack.pop()
        temp.reverse()
        pos.child+=temp
        stack.append(pos)
    elif s[i]==',':
        continue
    elif s[i]=='(':
        stack.append(s[i])
    else:
        stack.append(TreeNode(s[i]))

root=stack.pop()

def pre(tree):
    global pre_str
    pre_str+=tree.val
    for i in tree.child:
        pre(i)

def post(tree):
    global post_str
    for i in tree.child:
        post(i)
    post_str+=tree.val

pre_str=''
post_str=''
pre(root)
post(root)
print(pre_str)
print(post_str)
