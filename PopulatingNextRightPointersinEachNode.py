from typing import List
from typing import Optional

import collections

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        Q = collections.deque([root])
        
        while Q:
            
            size = len(Q)
            
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return root