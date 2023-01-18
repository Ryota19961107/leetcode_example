from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def removeNthFromEnd(self, head: Optional[TreeNode], n: int) -> Optional[TreeNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head