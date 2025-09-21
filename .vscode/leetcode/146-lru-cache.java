import java.util.HashMap;
import java.util.Map;

// Doubly Linked List for fast insert at end and pop at head 
class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    Map<Integer, Node> cache = new HashMap<>();
    int capacity;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head = new Node(0,0);
        this.tail = new Node(0,0);

        this.head.next = this.tail;
        this.tail.prev = this.head;

    }



    public void remove(Node node) {
        // Get prev and next
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next;
        next.prev = prev;
    }

    public void insert(Node node) {
        // insert at tail
        Node prev = this.tail.prev;
        Node next = this.tail;

        // set outside nodes
        prev.next = node;
        next.prev = node;

        // set inserted node
        node.prev = prev;
        node.next = next;

    }

    public int get(int key) {
        if (this.cache.containsKey(key)) {
            // get node
            Node tmp = this.cache.get(key);
            // delete and reinsert at tail
            remove(tmp);
            insert(tmp);
            return tmp.val;
        } else {
            return -1;
        }
    }

    public void put(int key, int val) {

        // if the node exists 
        if (this.cache.containsKey(key)) {

            // Get node and move to tail
            Node tmp = this.cache.get(key);
            remove(tmp);
            insert(tmp);

            // update with new value
            tmp.val = val;

        // otherwise it does not exist yet
        } else {

            // create, insert, add key:Node pair to hashmap
            Node tmp = new Node(key, val);
            insert(tmp);
            this.cache.put(key, tmp)
        }

        // constrain the cache size by capacity
        while (this.cache.size() > this.capacity) {
            Node tmp = this.head.next;
            remove(tmp);
            this.cache.remove(tmp.key);
        }
    }
}



/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */