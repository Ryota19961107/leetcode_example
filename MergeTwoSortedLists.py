from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        cur1 = list1
        cur2 = list2
        head = ListNode(0)
        cur = head
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next
        if not cur1:
            cur.next = cur2
        elif not cur2:
            cur.next = cur1
        return head.next
