# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def inLinkedelement(node:'TreeNode') -> bool:
            if not node:
                return False
            left = inLinkedelement(node.left)
            right = inLinkedelement(node.right)
            mid = node == p or node == q
            if left + right + mid >= 2:
                self.ans = node
            return left or right or mid
        
        inLinkedelement(root)
        return self.ans  