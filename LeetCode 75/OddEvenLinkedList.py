# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        odd:Optional[ListNode]=head        
        even:Optional[ListNode]=head.next
        evenHead:Optional[ListNode]=even

        while even and even.next:
            odd.next=even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next=evenHead
        return head
