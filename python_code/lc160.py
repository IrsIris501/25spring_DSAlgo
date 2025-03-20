# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        def list_node_len(head: ListNode) -> int:
            pointer=head
            ans=0
            while pointer:
                pointer=pointer.next
                ans+=1
            return ans
        len_a=list_node_len(headA)
        len_b=list_node_len(headB)
        pointer_a=headA
        pointer_b=headB
        if len_a>len_b:
            for i in range(len_a-len_b):
                pointer_a=pointer_a.next
        else:
            for i in range(len_b-len_a):
                pointer_b=pointer_b.next
        while pointer_b:
            if pointer_b==pointer_a:
                return pointer_b
            pointer_b=pointer_b.next
            pointer_a=pointer_a.next
        return None

        
