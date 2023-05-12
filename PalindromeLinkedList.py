# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        end_of_first_half = self.end_of_first_half(head)
        reversed_half = self.reverse_list(end_of_first_half.next)

        result = True
        first_ptr = head
        second_ptr = reversed_half
        while result and second_ptr is not None:
            if first_ptr.val!= second_ptr.val:
                result = False
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        end_of_first_half.next = self.reverse_list(reversed_half)
        return result


    def end_of_first_half(self, head):
        fast_ptr = head
        slow_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next
        return slow_ptr

    def reverse_list(self,head):
        current = head
        previous=None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
