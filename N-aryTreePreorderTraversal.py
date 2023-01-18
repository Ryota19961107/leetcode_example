from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution:
    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(reversed(node.children))
            
        return ans