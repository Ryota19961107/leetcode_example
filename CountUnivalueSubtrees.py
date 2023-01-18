from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def bottom_up(node: Optional[TreeNode], parent: int) ->bool:
            if not node:
                return True
            left = bottom_up(node.left, node.val)
            right = bottom_up(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent
        bottom_up(root, None)
        return self.ans