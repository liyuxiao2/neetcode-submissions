# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #base cases
        if len(lists) <= 2:
            if len(lists) == 0:
                return None
            return self.merge(lists[0], lists[1]) if len(lists) == 2 else self.merge(lists[0], [])

        mid = len(lists) // 2

        left = self.mergeKLists(lists[:mid + 1])
        right = self.mergeKLists(lists[mid+1:])

        return self.merge(right, left)

    def merge(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        new_head = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next
            new_head = new_head.next
        
        new_head.next = l1 or l2


        return dummy.next
