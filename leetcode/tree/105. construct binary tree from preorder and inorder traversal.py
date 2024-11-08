# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 하나씩 채워넣어야하지 않을까?
        # 전위 순회와 중위순회의 차이를 이해해야 한다.
        # 전위순회의 첫번째 녀석이 중위순회에서 정확히 반을 가른다.
        if inorder:
            idx = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx]) # 전위든.. 중위든... 어쨋든 한 노드 기준으로 나눠진것은 똑같으니까
            # 1이라면은... preorder에서 왼쪽을 모두 소모하고 오른쪽을 소모시켜 나가니까 자연스럽네..
            node.right = self.buildTree(preorder, inorder[idx + 1:])

            return node

