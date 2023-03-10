package LinkedList;

import java.util.HashSet;

/*142. Linked List Cycle II*/
public class no_142 {
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> set = new HashSet<>();
        while (head != null) {
            if (set.contains(head)) {
                return head;
            }
            set.add(head);
        }
        return null;
    }



}
