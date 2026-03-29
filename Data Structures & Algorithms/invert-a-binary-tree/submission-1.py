# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. 創一個跟原本數值一模一樣的新節點
        new_node = TreeNode(root.val)
        
        # 2. 讓新節點的「左手」去接「原本右邊反轉後的結果」
        new_node.left = self.invertTree(root.right)
        
        # 3. 讓新節點的「右手」去接「原本左邊反轉後的結果」
        new_node.right = self.invertTree(root.left)
        
        return new_node
            
