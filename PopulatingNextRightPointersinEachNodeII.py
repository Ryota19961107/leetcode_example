from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
            return prev, leftmost

    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root