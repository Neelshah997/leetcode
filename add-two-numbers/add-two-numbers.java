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
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        ListNode p = new ListNode(0);
        ListNode head = p;
        int ct= 0;
        int carry = 0;
        
        while(temp1!=null || temp2!=null){
            int x = carry;
            if (temp1!=null)
            {   x +=temp1.val;
                // ct++;
                temp1 = temp1.next;
            }
            if (temp2!=null)
            {
                x +=temp2.val;
                // ct++;
                temp2 = temp2.next;
            }
            if(x>9){
                carry=1;
                x = x-10;
            }   
            else{
                carry = 0;
            }
 
            ListNode l = new ListNode(x);
            head.next = l;
            head = head.next;
        }
        if(carry > 0){
        ListNode l = new ListNode(carry);
        head.next = l;
        }   
       return p.next;
    }
}