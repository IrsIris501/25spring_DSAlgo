from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_monotonic(l):
    if len(l) == 1:
        return 3
    else:
        if l[0] - l[1] > 0:
            last = l[0]
            for i in range(1, len(l)):
                if l[i] > last:
                    return False
                last = l[i]
            return 1
        else:
            last = l[0]
            for i in range(1, len(l)):
                if l[i] < last:
                    return False
                last = l[i]
            return 2

n = int(input())
traversal = deque(map(int, input().split()))
q = deque()
head = TreeNode(traversal[0])
q.append(head)
traversal.popleft()
alter = 0
while traversal:
    cur = q.popleft()
    if not alter:
        a = TreeNode(traversal.popleft())
        q.append(a)
        cur.left = a
        if traversal:
            a = TreeNode(traversal.popleft())
            q.append(a)
            cur.right = a


paths = []
def dfs(tree, path):
    if not tree.right and not tree.left:
        path.append(tree.val)
        paths.append(path)
        print(*path)
        return
    if tree.right:
        dfs(tree.right, path + [tree.val])
    if tree.left:
        dfs(tree.left, path + [tree.val])

dfs(head, [])

def is_heap(paths):
    ini = 3
    for i in range(len(paths)):

        if is_monotonic(paths[i]) == 3:
            continue
        elif is_monotonic(paths[i]) == 2:
            if ini == 1:
                print("Not Heap")
                return
            elif ini == 2:
                pass
            else:
                ini = 2
        elif is_monotonic(paths[i]) == 1:
            if ini == 2:
                print("Not Heap")
                return
            elif ini == 1:
                pass
            else:
                ini = 1
        else:
            print("Not Heap")
            return
    if ini == 1:
        print("Max Heap")
    elif ini == 2:
        print("Min Heap")

is_heap(paths)
