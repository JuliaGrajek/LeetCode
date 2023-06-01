# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMiddle(head:Optional[ListNode])->Optional[ListNode]:
            slow:Optional[ListNode]=head
            fast:Optional[ListNode]=head
            
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            if fast.next:
                slow=slow.next
            return slow
          
        
        
        prev:ListNode[Optional]=None
        curr:ListNode[Optional]=head
        nxt:ListNode[Optional]=head.next
        if nxt==None:
            return None
        middle=findMiddle(head)
        while curr is not middle:
            prev=curr
            curr=nxt
            nxt=curr.next
        prev.next=nxt
        return head
