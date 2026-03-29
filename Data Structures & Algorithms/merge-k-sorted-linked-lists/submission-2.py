# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node =ListNode(0)
        seen = []
        for lst in lists:
            while lst:
                seen.append(lst.val)
                lst = lst.next
        seen.sort() 
        for i in seen:
            node.next = ListNode(i)
            node = node.next
        return dummy.next  