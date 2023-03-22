package LinkedList;
/*2. Add Two Numbers*/
public class no_2 {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(1);
        ListNode node = head;
        int add = 0;
        int res = 0;
        int plus = 0;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                add = l2.val + plus;
                l2 = l2.next;
            } else if (l2 == null) {
                add = l1.val + plus;
                l1 = l1.next;
            } else {
                add = l1.val + l2.val + plus;
                l1 = l1.next;
                l2 = l2.next;
            }
            res = add % 10;
            plus = add / 10;
            node.next = new ListNode(res);
            node = node.next;
        }
        if (plus > 0) {
            node.next = new ListNode(plus);
        }
        return head.next;
    }

    public static void main(String[] args) {
        ListNode l1 = ListNode.makeListNode(new int[] {9,9,9,9,9,9,9});
        ListNode l2 = ListNode.makeListNode(new int[] {9,9,9,9});

        System.out.println(addTwoNumbers(l1, l2));
    }
}
