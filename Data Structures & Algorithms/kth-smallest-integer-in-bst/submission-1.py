class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while stack or current:
            # 先一路往左走到底，邊走邊把經過的節點放進 stack
            while current:
                stack.append(current)
                current = current.left

            # 彈出一個節點（也就是目前最小的還沒處理的節點）
            current = stack.pop()
            k -= 1

            # 如果這是第 k 小的節點
            if k == 0:
                return current.val

            # 往右子樹繼續找
            current = current.right
