package LinkedList;

import java.util.HashSet;
import java.util.Set;

/*141. Linked List Cycle*/
public class no_141 {
    public static boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<ListNode>();
        while (head != null) {
            if (set.contains(head)) {
                return true;
            } else {
                set.add(head);
                head = head.next;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        int[] arr = new int[] {3,2,0,-4};
        ListNode head = ListNode.makeListNode(arr);

        System.out.println(hasCycle(head));
    }
}
