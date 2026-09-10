# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast, slow = head.next, head

        while fast and fast.next:
            if slow.val == fast.val:
                return True
            print(slow.val, fast.val)

            fast = fast.next.next
            slow = slow.next
        
        return False