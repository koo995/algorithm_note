class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

sol = Solution()
sol.mergeTwoLists([1,2,4], [1,3,4])
# 클래스 안에 재귀호출하는 방식은 self을 안에 붙여줘야 하구나

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2개는 정렬되어 있는 리스트이다.
        # 이것을 하나의 정렬된 리스트로 만들어야한다.
        # 그냥 계속해서 비교하면 되는거 아닌가?
        if not list1 or not list2:
            return list1 or list2

        node = ListNode()
        if list1.val > list2.val:
            node.val = list2.val
            node.next = self.mergeTwoLists(list1, list2.next)
        else:
            node.val = list1.val
            node.next = self.mergeTwoLists(list1.next, list2)

        return node
