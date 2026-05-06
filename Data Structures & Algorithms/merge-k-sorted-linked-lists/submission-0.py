# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists)-1)
    
    def divide(self, lists, s, e):
        if s == e:
            return lists[s]
        if (e - s + 1) <= 1:
            return lists
        m = (s + e) //2
        left = self.divide(lists, s, m)
        right = self.divide(lists, m + 1, e)
        return self.merge(left, right)
    
    def merge(self, left, right):
        head = ListNode(-1)
        curr = head

        while left and right:
            l_val = left.val
            r_val = right.val

            if l_val <= r_val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        else:
            curr.next = right
        return head.next
                