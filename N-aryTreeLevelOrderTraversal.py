from typing import List
from typing import Optional

from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        quene = deque([root])
        while quene:
            size = len(quene)
            level = []
            for i in range(size):
                node = quene.popleft()
                level.append(node.val)
                for child in node.children:
                    quene.append(child)
            ans.append(level)
        return ans
        