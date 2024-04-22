# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
from collections import deque

class Codec:

    def serialize(self, root):
        queue = deque([root])
        result = ["#"]
        # 트리 bfs 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        # 예외처리
        if data == "# #":
            return None
        
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))