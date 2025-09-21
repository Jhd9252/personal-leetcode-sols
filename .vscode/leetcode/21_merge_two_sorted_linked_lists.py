# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        ''' In Place iterative'''
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy.next

    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        ''' 
        recursive
        Creates recrusion stack in order or smallest to largest
        Returns the next largest to above for assignment
        Base case is empty
        runtimet: O(n)
        Space: O(1)
        '''
        # base case, one list has ended
        if not list1:
            return list2
        if not list2:
            return list1
        # recurse (of the two current, set the next pointer of lowest)
        if list1.val < list2.val:
            # post process: assigns the result to this node
            list1.next = self.mergeTwoLists(list1.next, list2)
            # returns current node upward
            return list1
        else:
            # post process: assign result to this node
            list2.next = self.mergeTwoLists(list1, list2.next)
            # return this node up
            return list2
        
    