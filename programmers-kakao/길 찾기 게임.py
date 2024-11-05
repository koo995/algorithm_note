import sys

sys.setrecursionlimit(10 ** 6)


class TreeNode:
    def __init__(self, val=[], left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode[val: {self.val}, left: {self.left}, right: {self.right}]"


def solution(nodeinfo):  # x, y니까 유의하자.
    def bst(nodeinfo):
        if not nodeinfo:
            return None

        sorted_nodeinfo = sorted(nodeinfo, key=lambda node: (-node[1], node[0]))
        max_y_node = sorted_nodeinfo[0]
        idx = nodeinfo.index(max_y_node)

        node = TreeNode(max_y_node)
        node.left = bst(nodeinfo[:idx])
        node.right = bst(nodeinfo[idx + 1:])
        return node

    def front_search(node):
        if node:
            front_result.append(node_number_dic[node.val])
            front_search(node.left)
            front_search(node.right)
        return

    def back_search(node):
        if node:
            back_search(node.left)
            back_search(node.right)
            back_result.append(node_number_dic[node.val])
        return

    nodeinfo = list(map(tuple, nodeinfo))

    node_number_dic = {node: i for i, node in enumerate(nodeinfo, start=1)}

    node = bst(sorted(nodeinfo))

    # 자 이제 node을 탐색하자.
    front_result = []
    back_result = []
    front_search(node)
    back_search(node)

    answer = [front_result, back_result]
    return answer