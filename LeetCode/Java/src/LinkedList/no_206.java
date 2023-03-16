package LinkedList;

/*206. Reverse Linked List*/
public class no_206 {
    ListNode start = null;
    public ListNode reverse(ListNode head) {
        ListNode node = null;
        if (head != null){
            if (head.next != null) {
                node = reverse(head.next);
                node.next = new ListNode(head.val);
                node = node.next;
            }
            else {
                node = new ListNode(head.val);
                start = node;
            }
        }
        return node;
    }

    public ListNode reverseList(ListNode head) {
        ListNode node = reverse(head);
        return start;
    }

    public static void main(String[] args) {
        int[] arr = new int[] {1,2,3,4,5};
        ListNode head = ListNode.makeListNode(arr);

        System.out.println(new no_206().reverseList(head));
    }
}
