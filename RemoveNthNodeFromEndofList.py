class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
