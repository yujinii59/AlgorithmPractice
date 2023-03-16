package LinkedList;

/*234. Palindrome Linked List*/
public class no_234 {
    public static boolean isPalindrome(ListNode head) {
        ListNode reverseNode = null;
        while (head != null) {
            ListNode node = new ListNode(head.val);
            node.next = reverseNode;
            reverseNode = node;
            if (reverseNode == head.next) return true;
            if (reverseNode == head) return true;
            head = head.next;
        }

        return false;
    }

    public static void main(String[] args) {
        int[] ls = new int[]{1,2,2,1};
        ListNode head = ListNode.makeListNode(ls);
        System.out.println(isPalindrome(head));
    }
}
