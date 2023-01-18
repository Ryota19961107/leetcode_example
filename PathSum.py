from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        self.flag = False
        def PathSum(node: Optional[TreeNode], remain: int) ->bool:
            if not node:
                return
            if remain == node.val and not node.left and not node.right:
                self.flag = True
            
            PathSum(node.left, remain - node.val)
            PathSum(node.right, remain - node.val)
            
            return self.flag
        
        return PathSum(node = root, remain = targetSum)