
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def prt(self):
        while self:
            print(self.val, end=' ')
            self = self.next
        print()
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next




        prev=None
        while slow:
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node

        cur1=head
        cur2=prev

        while cur1.next!=None:
            if cur1.val!=cur2.val:
                return False
            cur1=cur1.next
            cur2=cur2.next
        return True


#s=Solution()
#l=list(map(int, input().split()))
#l.reverse()
#head=None
#for i in l:
#    head=ListNode(i, head)
#print(s.isPalindrome(head))

