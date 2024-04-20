# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        from collections import deque
        
        if root is None:
            return 0
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # 흠.. 이렇게 하면 현재 루트노드의 갯수만큼 모두다 뽑아내는 것인가
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth
        
    
    def maxDepth1(self, root) -> int:
        from collections import deque

        if root is None:
            return 0
            
        q = deque()
        q.append((root, 1))
        max_level = -1
        while q:
            node, level = q.popleft()
            max_level = max(max_level, level)
            l_node = node.left
            r_node = node.right
            if l_node != None:
                q.append((l_node, level + 1))
            if r_node != None:
                q.append((r_node, level + 1))
        return max_level