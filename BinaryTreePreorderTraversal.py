from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

         
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]

        while stack:
            cur_node = stack.pop()
            if cur_node:
                ans.append(cur_node.val)
                stack.append(cur_node.right)
                stack.append(cur_node.left)
        
        return ans