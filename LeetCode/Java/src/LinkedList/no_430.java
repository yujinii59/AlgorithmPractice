package LinkedList;

/*430. Flatten a Multilevel Doubly Linked List*/
public class no_430 {
    public ChildNode flatten(ChildNode head) {
        if (head == null) return null;
        ChildNode head_node = new ChildNode();
        ChildNode node = head_node;
        node.val = head.val;
        if (head.child != null) {
            ChildNode child = flatten(head.child);
            child.prev = node;
            node.next = child;
            while (node.next != null) {
                node = node.next;
            }
        }
        if (head.next != null) {
            ChildNode next = flatten(head.next);
            next.prev = node;
            node.next = next;
        }

        return head_node;
    }
}
