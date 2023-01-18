from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

         
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left: int, in_right):
            if in_left > in_right:
                return
            
            val = preorder.pop(0)
            index = idx_map[val]
            node = TreeNode(val)
            
            node.left = helper(in_left, index - 1)
            node.right = helper(index + 1, in_right)
            
            return node
        
        idx_map = {v : i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)     