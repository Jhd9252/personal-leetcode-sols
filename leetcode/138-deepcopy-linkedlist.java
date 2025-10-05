

class Node {
    int val;
    Node next;
    Node random;

    Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Map<Node, Node> map = new HashMap<>();
        Node curr = head;
        // first pass -> create and primitive
        while (curr != null) {
            map.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        // second pass - link to newly created 
        curr = head;
        while (curr != null) {
            map.get(curr).next = map.get(curr.next);
            map.get(curr).random = map.get(curr.random);
        }

        // return 
        return map.get(head);
    }
}
