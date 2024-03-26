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