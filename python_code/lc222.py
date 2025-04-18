from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    bfs method
    def countNodes(self, root: TreeNode) -> int:
        ans=0
        if not root:
            return ans
        q=deque()
        q.append(root)
        while q:
            pos=q.popleft()
            ans+=1
            if pos.left:
                q.append(pos.left)
            if pos.right:
                q.append(pos.right)
        return ans
    '''

    def countNodes(self, root: TreeNode) -> int:
        '''
        binary search
        '''
        h=0
        if not root:
            return 0
        q=deque()
        q.append(root)
        while q:
            pos=q.popleft()
            h+=1
            if pos.left:
                q.append(pos.left)
        left=2**(h-1)
        right=2**h
        while right-left!=1:
            mid=(left+right)//2
            mid_bin=str(bin(mid))
            i=3
            pos=root
            avail=True
            while i<len(mid_bin):
                if int(mid_bin[i]):
                    if pos.right:
                        pos=pos.right
                        i+=1
                    else:
                        avail=False
                        break
                else:
                    if pos.left:
                        pos=pos.left
                        i+=1
                    else:
                        avail=False
                        break
            if avail:
                left=mid
            else:
                right=mid
        return left





