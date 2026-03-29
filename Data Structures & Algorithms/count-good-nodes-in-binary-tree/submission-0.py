class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node, max_so_far):
            if not node:
                return
            
            # 1. 檢查自己是不是「好節點」
            # 如果我比路徑上出現過的最高分還大（或相等），我就是好節點！
            if node.val >= max_so_far:
                self.count += 1
                # 更新這條路徑上的「最高分紀錄」
                max_so_far = node.val
            
            # 2. 帶著「這條路目前的最高分」去問左邊跟右邊的小孩
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
            
        # 一開始的「最高分」就是根節點的值
        dfs(root, root.val)
        return self.count