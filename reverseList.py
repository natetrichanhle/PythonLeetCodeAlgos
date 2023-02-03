class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # iterative solution 
        # prev, curr = None, head

        # while curr:
        #     # need to instantiate a temp variable since curr.next is assigned to prev and you need to iterate the curr to the next node
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

        # recursive solution

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead