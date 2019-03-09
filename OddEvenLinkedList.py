# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)
        even = ListNode(0)
        oddHead,evenHead = odd,even
        
        index = 0
        
        while head:
            if index%2 == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            index = index + 1
            head = head.next
        even.next = None
        odd.next = evenHead.next
        
        return oddHead.next
