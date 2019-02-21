# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: 'ListNode', k: 'int') -> 'List[ListNode]':
        nodes = []
        count = 0
        each = root
        while each:
            each = each.next
            count = count + 1
        num = count//k
        rem = count%k
        
        for i in range(k):
            head = ListNode(0)
            each = head
            for j in range(num):
                node = ListNode(root.val)
                each.next = node
                each = each.next
                root = root.next
            if rem and root:
                rmnode = ListNode(root.val)
                each.next = rmnode
                if root:
                    root = root.next
                rem = rem - 1
            nodes.append(head.next)
            
        return nodes
