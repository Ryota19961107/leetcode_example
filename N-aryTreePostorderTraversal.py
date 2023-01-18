from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        def recursion(node):
            if not node:
                return
            for child in node.children:
                recursion(child)
            ans.append(node.val)
        recursion(root)
        return ans