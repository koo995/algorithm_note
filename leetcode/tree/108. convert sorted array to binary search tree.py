# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        root_node = TreeNode(nums[mid])
        root_node.left = self.sortedArrayToBST(nums[:mid])
        root_node.right = self.sortedArrayToBST(nums[mid + 1:])
        return root_node


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 이진탐색트리로 어떻게 변환할까?
        # 생각을해보자. 루트기준으로 좌가 작은것 우가 큰것이다.
        # 정렬된 숫자들이 주어딘다.
        # 이진탐색트리이면... 루트노드는 무엇이지? 가장 가운데 값이 되면 될 것 같다.
        if not nums:
            return None

        mid = len(nums) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))
