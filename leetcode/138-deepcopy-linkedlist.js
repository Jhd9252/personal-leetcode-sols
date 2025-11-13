
const copyRandomList = (head) => {
    if (!head) return null;
    const mapper = new Map();
    let curr = head;
    while (curr) {
        mapper.set(curr, new Node(curr.val));
        curr = curr.next;
    }

    curr = head;
    while (curr) {
        mapper.get(curr).next = mapper.get(curr.next) || null;
        mapper.get(curr).random = mapper.get(curr.random) || null;
        curr = curr.next;
    }
    return mapper.get(head);
}