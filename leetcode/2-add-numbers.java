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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode nHead = new ListNode();
        ListNode curr = nHead;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int num1 = (l1 != null) ? l1.val : 0;
            int num2 = (l2 != null) ? l2.val : 0;

            int sum = num1 + num2 + carry;
            int actual = sum % 10;
            carry = sum / 10; // integer truncated downwards towards zero

            curr.next = new ListNode(actual);
            curr = curr.next;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;

            // if end and still carry, 0 + 0 + 1, next is 0 0 0 which loop doesnt start
        }
        return nHead.next;
        

    }
}