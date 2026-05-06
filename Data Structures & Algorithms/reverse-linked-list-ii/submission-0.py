# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        leftPointer = dummy
        for _ in range(left - 1):
            leftPointer = leftPointer.next
        start = leftPointer.next

        prev = None
        for _ in range(right - left + 1):
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        
        leftPointer.next.next = start
        leftPointer.next = prev
        return dummy.next