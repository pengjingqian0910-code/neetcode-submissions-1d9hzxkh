from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: 建立一個虛擬頭節點
        # 這樣做的好處是：如果我們要刪除的節點是原鏈表的頭節點，
        # 我們也可以用統一的方式處理，不需要額外判斷。
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: 第一次遍歷，計算鏈表的總長度 L
        current = dummy.next # 從實際的頭節點開始計數
        length = 0
        while current:
            length += 1
            current = current.next

        # Step 3: 計算要遍歷多少步才能到達「要刪除節點的前一個節點」
        # 要刪除的是倒數第 n 個節點，也就是從頭數來的第 (length - n + 1) 個節點。
        # 我們需要找到它前面一個節點，也就是第 (length - n) 個節點。
        # 因為我們是從 dummy 節點開始遍歷，所以實際上需要移動 (length - n) 步。
        steps_to_reach_prev = length - n

        # 如果 steps_to_reach_prev < 0，表示 n 太大（超過鏈表長度），
        # 雖然題目通常會保證 n 有效，但這裡是為了思路完整性。
        if steps_to_reach_prev < 0:
            return head # 實際上題目保證 n 有效，不會發生這種情況

        # Step 4: 第二次遍歷，找到目標節點的前一個節點
        current = dummy # 從虛擬頭節點開始遍歷

        # 移動 steps_to_reach_prev 步
        for _ in range(steps_to_reach_prev):
            current = current.next

        # 現在 current 指向的就是「要刪除節點的前一個節點」
        # 我們要刪除的節點是 current.next
        # 將 current.next 指向 current.next.next，即可跳過目標節點，完成刪除
        if current.next: # 確保 current.next 不是 None，避免出錯（雖然在有效輸入下不會）
             current.next = current.next.next
        else:
            # 這表示 steps_to_reach_prev 把 current 移到了鏈表的末尾，
            # current.next 已經是 None，這通常不應該發生在有效移除操作中
            # 但作為防禦性編程可以加上
            pass 
        

        # 最後，回傳虛擬頭節點的下一個節點，它就是新鏈表的頭節點
        return dummy.next