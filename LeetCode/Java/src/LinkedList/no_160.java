package LinkedList;

import java.util.HashSet;

/*160. Intersection of Two Linked Lists*/
public class no_160 {

    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> setA = new HashSet<>();
        HashSet<ListNode> setB = new HashSet<>();
        while (headA != null || headB != null) {
            if (headA != null) {
                if (setB.contains(headA)) return headA;
                setA.add(headA);
                headA = headA.next;
            }
            if (headB != null) {
                if (setA.contains(headB)) return headB;
                setB.add(headB);
                headB  = headB.next;
            }

        }
        return null;
    }

    public static void main(String[] args) {

    }
}
