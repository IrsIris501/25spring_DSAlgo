# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def prt(self):
        pointer=self
        while pointer:

            print(pointer.val, end=' ')
            pointer=pointer.next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast=head
        slow=head
        if fast.next==None:
            return None
        for i in range(n):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next

        return head.next

s=Solution()
listnode=ListNode()

lst=list(map(int, input().split()))

lst.reverse()
lst.append('start_mark')
head=None
for i in lst:
    head=ListNode(i, head)

n=int(input())
output=s.removeNthFromEnd(head, n)
output.prt()



