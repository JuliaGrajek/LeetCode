# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_ptr: ListNode = head
        slow_ptr: ListNode = head
        
        while fast_ptr.next is not None:
            if fast_ptr.next.next is not None:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        
        return slow_ptr
