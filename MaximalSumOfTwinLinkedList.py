# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst: List[int]=[]
        node: Optional[ListNode]=head
        max_sum:int=-inf
        tmp:int=0
        while node:
            lst.append(node.val)
            node=node.next
        for i in range(len(lst)//2):
            tmp = lst[i]+lst[len(lst)-1-i]
            if tmp>max_sum:
                max_sum=tmp
        return max_sum
