# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        start, end = dummy, dummy

        i = 1
        iter_head = head
        while iter_head and i <= right:
            if i == left - 1:
                start = iter_head
            if i == right:
                end = iter_head.next

            iter_head = iter_head.next
            i += 1

        iter_head = start.next
        prev = end

        for _ in range(right - left + 1):
            nxt = iter_head.next

            iter_head.next = prev

            prev = iter_head
            iter_head = nxt

        tail = start.next
        start.next = prev
        tail.next = iter_head

        return dummy.next
        
