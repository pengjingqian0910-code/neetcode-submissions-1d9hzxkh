# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = []
        res = []
        q.append(root)
        while q :
            sub = []
            Qlen = len(q)
            for _ in range(Qlen):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sub.append(node.val)
            if sub:
                right = sub.pop(-1)
                res.append(right)
        return res

        