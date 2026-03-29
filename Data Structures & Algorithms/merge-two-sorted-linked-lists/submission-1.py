# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        # 2. 派出施工車 curr，一開始停在車站
        curr = dummy
        
        # 只要兩條舊鐵路都還有材料
        while list1 and list2:
            if list1.val <= list2.val:
                # 把小的接過來
                curr.next = list1
                # 舊鐵路往後移
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            # 施工車往前開一格，停在剛接好的那一節上面
            curr = curr.next
            # 3. 如果有一條鐵路用完了，另一條還有剩，就直接整段接上去
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
            
        # 4. 永遠回傳車站（dummy）的下一個，那才是新火車的頭！
        return dummy.next