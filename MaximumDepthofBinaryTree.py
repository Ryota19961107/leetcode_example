from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        self.ans = 0
        def preorder(node, depth:int) -> int:
            if not node:
                return
            if not node.left and not node.right:
                self.ans = max(self.ans, depth)
            preorder(node.left, depth + 1)
            preorder(node.right, depth + 1)
        
        preorder(root, 1)
        return self.ans   