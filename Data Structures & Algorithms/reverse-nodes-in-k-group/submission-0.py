# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            #find the k nodes
            end_rev = self.findkthNode(groupPrev, k)
            if not end_rev:
                break
            
            next_grp = end_rev.next

            prev, curr = end_rev.next, groupPrev.next
            while curr != next_grp:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = end_rev
            groupPrev = tmp
        
        return dummy.next

        

    def findkthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur