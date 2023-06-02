# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tmp:int=0
        max_sum:int=-inf
        tail:Optional[ListNode]


        def reverse_list(head: Optional[ListNode])->Optional[ListNode]:
            prev:Optional[ListNode]=None
            current:Optional[ListNode]=head
            k:int=0
            while current:
                nxt=current.next
                current.next=prev
                prev = current
                current=nxt      
            return prev
        
        def find_end_of_first_half(head: Optional[ListNode])->Optional[ListNode]:
            slow:Optional[ListNode]=head
            fast:Optional[ListNode]=head
            while  fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            return slow

        end_of_half = find_end_of_first_half(head)
        tail = reverse_list(end_of_half.next)

        while tail:
         
            tmp = head.val+tail.val
            if tmp>max_sum:
                max_sum=tmp
            head=head.next
            tail=tail.next
        return max_sum
      
      #OR, EASIER APPROACH BUT REQUIRES THE CREATION OF AN ADDITIONAL LIST
      
#       class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         lst: List[int]=[]
#         node: Optional[ListNode]=head
#         max_sum:int=-inf
#         tmp:int=0
#         while node:
#             lst.append(node.val)
#             node=node.next
#         for i in range(len(lst)//2):
#             tmp = lst[i]+lst[len(lst)-1-i]
#             if tmp>max_sum:
#                 max_sum=tmp
#         return max_sum
