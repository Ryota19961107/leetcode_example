from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def isPalindrome(self, head: Optional[TreeNode]) -> bool:
        if not head :
            return False
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        l, r  = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True