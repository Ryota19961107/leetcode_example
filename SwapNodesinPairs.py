from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        current = dummyhead
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            current.next = second
            first.next = second.next
            second.next = first
            current = first
        return dummyhead.next