package LinkedList;

/*203. Remove Linked List Elements*/
public class no_203 {
    public static ListNode removeElements(ListNode head, int val) {
        ListNode head_node = null;
        ListNode node = null;
        while (head != null) {
            if (head.val != val) {
                if (head_node != null) {
                    node.next = new ListNode(head.val);
                    node = node.next;
                } else {
                    head_node = new ListNode(head.val);
                    node = head_node;
                }
            }
            head = head.next;
        }

        return head_node;
    }

    public static void main(String[] args) {
        int[] ls = new int[] {1,2,6,3,4,5,6};
        ListNode head = ListNode.makeListNode(ls);
        System.out.println(removeElements(head, 6));
    }
}
