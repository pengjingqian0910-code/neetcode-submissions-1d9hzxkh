# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. 準備一個世界紀錄保持者（變數）
        self.max_dia = 0
        def dfs(node):
            if not node:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            self.max_dia = max(self.max_dia,left_h + right_h )
            return max(left_h, right_h) + 1
        dfs(root)
        return self.max_dia