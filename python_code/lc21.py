# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def prt(self):
        temp=self
        while temp:
            print(temp.val, end=' ')
            temp=temp.next
        print()

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        def reverse(head: ListNode):
            prev=None
            while head:
                next_node=head.next
                head.next=prev
                prev=head
                head=next_node
            return prev
        list1=reverse(list1)
        list2=reverse(list2)
        print('reversed')
        ans=None
        while list1 and list2:
            if list1.val>list2.val:
                ans=ListNode(list1.val, ans)
                list1=list1.next
            else:
                ans=ListNode(list2.val, ans)
                list2=list2.next
        while list1:
            ans=ListNode(list1.val, ans)
            list1=list1.next
        while list2:
            ans=ListNode(list2.val, ans)
            list2=list2.next
        print('returned')
        return ans
        
s=Solution()
list1=list(map(int, input().split()))
list2=list(map(int, input().split()))
head1=None
head2=None
while list1:
    temp=list1.pop()
    head1=ListNode(temp, head1)
while list2:
    temp=list2.pop()
    head2=ListNode(temp, head2)
a=s.mergeTwoLists(head1, head2)
a.prt()