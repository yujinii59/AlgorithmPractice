package LinkedList;

import java.util.HashMap;

/*138. Copy List with Random Pointer*/
public class no_138 {
    public RandomNode copyRandomList(RandomNode head) {
        HashMap<RandomNode, RandomNode> map = new HashMap<>();
        RandomNode hnode = head;
        RandomNode node = new RandomNode(0);
        while (hnode != null) {
            RandomNode randomNode = new RandomNode(hnode.val);
            map.put(hnode, randomNode);
            node.next = randomNode;
            node = node.next;
            hnode = hnode.next;
        }
        RandomNode headNode = map.get(head);
        while (head != null) {
            if (head.random != null) map.get(head).random = map.get(head.random);
            head = head.next;
        }

        return headNode;
    }
}
