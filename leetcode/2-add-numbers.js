const addTwoNumbers = (l1, l2) => {
    let nHead = new ListNode();
    let curr = nHead;
    let carry = 0;

    while (l1 || l2 || carry) {
        // conditional nums -> && syntax is var = this () if this ()
        let n1 = l1 && l1.val;
        let n2 = l2 && l2.val;

        // get total
        let sum = n1 + n2 + carry;

        // set next carry
        carry = Math.floor(sum/10);

        // create and set next node floor div
        curr.next = new ListNode(sum%10);

        // move pointers -> else leave at null
        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;

        curr = curr.next;

    }

    return nHead.next;
}