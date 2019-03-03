# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self,root):
        if root.left == None and root.right == None:
            return True
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        s = 0
        if root.left and self.isLeaf(root.left):
            s += root.left.val
            
        return s + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
