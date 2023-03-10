package LinkedList;

import java.util.HashMap;

/*19. Remove Nth Node From End of List*/
public class no_19 {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode node = head;
        HashMap<Integer, ListNode> map = new HashMap<>();
        int i = 0;
        while (node != null) {
            map.put(i, node);
            node = node.next;
            i++;
        }
        if (i-n == 0) {
            head = head.next;
        } else if (n == 1) {
            map.get(i-2).next = null;
        } else {
            map.get(i - n - 1).next = map.get(i - n + 1);
        }

        return head;
    }

}
