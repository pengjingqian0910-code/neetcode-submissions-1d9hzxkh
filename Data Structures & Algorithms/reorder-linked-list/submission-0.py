class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 找中間節點
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反轉後半段
        prev = None
        curr = slow.next
        slow.next = None  # 切斷前後半段
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # 3. 合併前後半段（head 與 prev）
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
