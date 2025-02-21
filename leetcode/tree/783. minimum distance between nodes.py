# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    max_value = -sys.maxsize
    min_value = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.min_value = min(self.min_value, root.val - self.max_value)
        self.max_value = max(self.max_value, root.val)

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_value




    def minDiffInBST2(self, root: Optional[TreeNode]) -> int: # 이것은 초기에 내가 나아갈려는 방향이엇으나... 잘못되었다.
        def find_max(root):
            if not root:
                return 0

            max_right = find_max(root.right)
            self.min_value = min(self.min_value, abs(root.val - max_right))
            return max_right

        def find_min(root):
            if not root:
                return int(1e9)
            min_left = find_min(root.)
            # 아하 노드간의 값의 차이가 가장 작은 노드의 갑스차이를 출력해야하군?

        # 우선 BST로 주어진다. 탐색이 이루어져야 하고... 각 노드에서 왼쪽을 탐색한다면 가장 큰 값 오른쪽을 탐색한다면 가장 작은 값을 찾아서 현재 값과 비교하면 될듯?

        left_max = find_max(root.left)
        right_min = find_min(root.right)
        min_value = min(min_value, abs(root.val - left_max), abs(root.val - right_min))
        return self.min_value


class Solution2:
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return

        self.minDiffInBST(root.left)
        # evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

