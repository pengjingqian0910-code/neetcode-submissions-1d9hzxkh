# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = right = dummy
        while(n + 1>0):
            n-=1
            right = right.next
        while right:
            right = right.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next