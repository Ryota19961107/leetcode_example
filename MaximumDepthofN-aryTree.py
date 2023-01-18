# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def depth(node) -> int:           
            ans = 1
            if not node.children:
                return ans
            for child in node.children:
                ans = max(ans, 1 + depth(child))
            return ans
        return depth(root)