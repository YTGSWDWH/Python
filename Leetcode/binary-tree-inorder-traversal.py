class Solution:
    def inorderTraversal(self, root):
        res = []
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = root
                temp =root
                root = root.left
                temp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res