# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if not lists or len(lists) == 0:
            return None
        
        # take pairs of linked lists and merge until there's only 1 remaining
        while len(lists) > 1:
            # mergedList is instantiated to put the 2 merged lists into 1 list
            mergedList = []
            # we increment by 2 because we are working with pairs of linked lists
            for i in range (0, len(lists), 2):
                l1 = lists[i]
                # if we have an odd num of lists and we increment by 2 each time, this can be out of bounds so we need the base case
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # append the 2 lists into the mergedList
                mergedList.append(self.mergeTwoLists(l1, l2))
            # update our lists variable (mergedLists is like a temp var)
            lists = mergedList
        # return when there's only 1 list left
        return lists[0]
    
    # same algo as mergeTwoLists
    def mergeTwoLists(self, list1, list2):
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