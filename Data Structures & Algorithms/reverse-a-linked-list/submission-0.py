# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None

        # iterating & reversing from the start
        curr, prev = head, None
        while curr:
            # grab the next
            next_temp = curr.next
            # turn around
            curr.next = prev
            # move prev to forward
            prev = curr
            # move forward
            curr = next_temp
        
        # return (prev as new head)
        return prev