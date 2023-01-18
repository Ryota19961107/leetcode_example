from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

         
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left: int, in_right: int):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            index = idx_map[val]
            
            node.right = helper(index + 1, in_right)
            node.left = helper(in_left, index - 1)
            
            return node
        
        idx_map = {v : i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)