# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if (i + 1) < len(lists) else None
                temp.append(self.mergeNode(first, second))
            lists = temp
        return lists[0]

    def mergeNode(self, first, second):
        dummy = ListNode(0)
        curr = dummy

        while first and second:
            if first.val <= second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next
        
        if first:
            curr.next = first
        if second:
            curr.next = second
        return dummy.next