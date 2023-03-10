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

        System.out.println(hasCycle(head));
    }
}

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }
