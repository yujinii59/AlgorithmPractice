package LinkedList;

/*21. Merge Two Sorted Lists*/
public class no_21 {
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(1);
        ListNode node = head;
        while (list1 != null || list2 != null) {
            if (list1 == null) {
                node.next = new ListNode(list2.val);
                list2 = list2.next;
            } else if (list2 == null) {
                node.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                int val1 = list1.val;
                int val2 = list2.val;
                if (val1 < val2) {
                    node.next = new ListNode(val1);
                    list1 = list1.next;
                } else {
                    node.next = new ListNode(val2);
                    list2 = list2.next;
                }
            }
            node = node.next;
        }

        return head.next;
    }

    public static void main(String[] args) {
        int[] list1 = new int[] {1,2,4};
        int[] list2 = new int[] {1,3,4};
        ListNode node1 = ListNode.makeListNode(list1);
        ListNode node2 = ListNode.makeListNode(list2);

        System.out.println(mergeTwoLists(node1, node2));
    }
}
