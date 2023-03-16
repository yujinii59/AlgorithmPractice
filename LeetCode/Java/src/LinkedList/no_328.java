package LinkedList;

/*328. Odd Even Linked List*/
public class no_328 {
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = null;
        ListNode even = null;
        ListNode oddHead = null;
        ListNode evenHead = null;
        while (head != null && head.next != null){
            if (oddHead != null){
                odd.next = new ListNode(head.val);
                odd = odd.next;
                even.next = new ListNode(head.next.val);
                even = even.next;
            } else {
                oddHead = new ListNode(head.val);
                odd = oddHead;
                evenHead = new ListNode(head.next.val);
                even = evenHead;
            }

            head = head.next.next;
        }

        if (head != null) {
            if (oddHead != null){
                odd.next = new ListNode(head.val);
                odd = odd.next;
            } else {
                oddHead = new ListNode(head.val);
                odd = oddHead;
            }
        }

        if (odd != null) {
            odd.next = evenHead;
        }

        return oddHead;

    }
}
