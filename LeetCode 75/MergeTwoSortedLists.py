# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1:Optional[ListNode]=list1
        ptr2:Optional[ListNode]=list2
        head: Optional[ListNode]
   
        if ptr1 is None and ptr2 is None:
            return ptr1
        elif ptr1 is None:
            return ptr2
        elif ptr2 is None:
            return ptr1
        else:
          
            if ptr1.val<=ptr2.val:
                list3=list1
                ptr1=ptr1.next
                head=list3
            else:
                list3=list2
                ptr2=ptr2.next
                head=list3
            
            while ptr1 is not None and ptr2 is not None:
                if ptr1.val<=ptr2.val:
                    list3.next=ptr1
                    list3=list3.next
                    ptr1=ptr1.next
                else:
                    list3.next=ptr2
                    list3=list3.next
                    ptr2=ptr2.next
            
            if ptr1 is None:
                list3.next = ptr2
             
            elif ptr2 is None:
                list3.next=ptr1
            return head
