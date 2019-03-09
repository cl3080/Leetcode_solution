# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = []
        leaf2 = []
        
        self.inOrder(root1,leaf1)
        self.inOrder(root2,leaf2)

        return leaf1 == leaf2
    
    def inOrder(self, root, leaf):
        if not root:
            return 
        self.inOrder(root.left,leaf)
        if not root.left and not root.right:
            leaf.append(root.val)
        self.inOrder(root.right,leaf)
