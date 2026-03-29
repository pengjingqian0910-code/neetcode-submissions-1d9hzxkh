def get_path(root, target):
    path = []
    while root:
        path.append(root)
        if target.val < root.val:
            root = root.left
        elif target.val > root.val:
            root = root.right
        else:
            break
    return path

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        path_p = get_path(root, p)
        path_q = get_path(root, q)

        lca = None
        for u, v in zip(path_p, path_q):
            if u == v:
                lca = u
            else:
                break
        return lca
