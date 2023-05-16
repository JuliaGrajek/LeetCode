# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        previous = None
        n = head.next
        curr=head
        while curr.next is not None:
            curr.next=previous
            previous = curr
            curr = n
            n = curr.next
        curr.next = previous
        return curr
    
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseListRecu(head):
            if not head or not head.next: return head
            node, head.next.next, head.next = reverseListRecu(head.next), head, None
            return node
        return reverseListRecu(head)
