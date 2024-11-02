# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1증가
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):

            if not root:
                return 0
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            if left_node == -1 or right_node == -1:
                return -1
            if abs(left_node - right_node) > 1:
                return -1
            return max(left_node, right_node) + 1

        result = dfs(root)
        return True if result != -1 else False