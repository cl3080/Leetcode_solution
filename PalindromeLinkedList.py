# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        p = slow
        last = None
        while p:
            newhead = p.next
            p.next = last
            last = p
            p = newhead
            
        p1 = head
        p2 = last
        
        while p1 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        return p1 is None
