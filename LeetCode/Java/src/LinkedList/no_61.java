package LinkedList;

import java.util.HashMap;

/*61. Rotate List*/
public class no_61 {

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;
        int i = 0;
        HashMap<Integer, ListNode> map = new HashMap<>();
        while (head != null) {
            map.put(i++, head);
            head = head.next;
        }

        k = k % i;
        head = map.get(0);
        for (int j = 0; j < k; j++) {
            map.get(i-1-j).next = head;
            map.get(i-2-j).next = null;
            head = map.get(i-1-j);
        }

        return head;
    }
}
