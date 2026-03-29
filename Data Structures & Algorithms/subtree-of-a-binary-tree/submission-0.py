from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        queue = deque([root])

        while queue:
            node = queue.popleft()
            # 如果目前節點值與 subRoot 相同，就檢查整棵子樹是否相同
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True
            # BFS 逐層探索
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        # 遞迴檢查左右子樹
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
