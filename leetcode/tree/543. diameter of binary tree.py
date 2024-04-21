# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest_distance = -1
    
    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node):
            # 언제 탐색을 그만둘 것이냐?
            if not node:
                return -1
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            # 현재 노드에서 최대 거리는?
            self.longest_distance = max(self.longest_distance, left_node + right_node + 2)
            # 현재 노드에서 상태값은?
            return max(left_node, right_node) + 1

        dfs(root)
        return self.longest_distance
        
