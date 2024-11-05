# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            self.result += node.val if low <= node.val <= high else 0
            if node.val <= high:
                dfs(node.right)
                # 오른쪽 탐색하면 안됨.
            if node.val >= low:
                # 왼쪽 탐색하면 안됨.
                dfs(node.left)

        dfs(root)
        return self.result