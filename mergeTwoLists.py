# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # loop through both lists
        # compare values at each node since it's already sorted
        # insert values into the output if conditions are met
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # if there are still values in one of the lists
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # we return dummy.next because we don't want to account for the dummy node that we instantiated in the beginning
        return dummy.next