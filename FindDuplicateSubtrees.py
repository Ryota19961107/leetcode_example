from collections import defaultdict
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        import collections
        def traverse(node):
            if not node:
                return ""
            representation = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            cnt[representation] += 1
            if cnt[representation] == 2:
                res.append(node)
            return representation
        
        res = []
        cnt = defaultdict(int)
        traverse(root)
        return res