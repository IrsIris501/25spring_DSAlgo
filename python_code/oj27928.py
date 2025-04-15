class TreeNode:
    def __init__(self, val):
        self.val=val
        self.child=[]


n=int(input())
node_dict=dict()
all_node=set()
children_node=set()
for i in range(n):
    l=list(map(int, input().split()))
    node_dict[l[0]]=l[1::]
    all_node.add(l[0])
    children_node.update(l[1::])
    if i==0:
        root_val=l[0]

root_val=(all_node-children_node).pop()
def build_tree(root_val):
    root=TreeNode(root_val)
    for i in node_dict[root_val]:
        root.child.append(build_tree(i))
    return root

tree=build_tree(root_val)
traversal_list=[]
def traverse(tree: TreeNode, last=None):
    if not tree.child:
        traversal_list.append(tree.val)
        return
    if tree==last:
        traversal_list.append(tree.val)
        return
    temp=tree.child+[tree]
    temp.sort(key=lambda x: x.val)
    for i in range(len(temp)):
        traverse(temp[i], tree)

traverse(tree)
print(*traversal_list, sep='\n')







