# Definition for singly-linked list.
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next_node: ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


sol = Solution()
l = [1, 2, 3, 4, 5]
for idx, value in enumerate(l[:-1]):
    linked_list = ListNode(value, None)
    linked_list.next_node = ListNode(l[idx + 1], None)

print("input: ", linked_list)
# sol.reverseList()
