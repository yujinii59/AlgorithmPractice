package LinkedList;

public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        this.val = x;
        this.next = null;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode makeListNode(int[] arr) {
        ListNode head = null;
        ListNode node = null;
        for (int num : arr) {
            if (head == null) {
                head = new ListNode(num);
                node = head;
            } else {
                node.next = new ListNode(num);
                node = node.next;
            }
        }
        return head;
    }
}
