# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root

class Solution2:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(root, s):
            if not root:
                return None, s

            right, s = postorder(root.right, s)
            val = root.val + s
            s = val
            left, s = postorder(root.left, s)
            return TreeNode(val, left, right), s

        result, _ = postorder(root, 0)
        return result
