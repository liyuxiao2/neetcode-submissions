/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode scnd = slow.next;
        ListNode prev = slow.next = null;

        while (scnd != null) {
            ListNode tmp = scnd.next;
            scnd.next = prev;
            prev = scnd;
            scnd = tmp;
        }

        ListNode first = head;
        while(prev != null) {
            ListNode dum1 = prev.next;
            ListNode dum2 = first.next;

            first.next = prev;
            prev.next = dum2;
            first = dum2;
            prev =  dum1;
        }
    }
}
