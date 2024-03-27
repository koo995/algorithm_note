class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dic = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            if ch == ")" or ch == "}" or ch == "]":
                if stack and parentheses_dic[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


sol = Solution()
sol.isValid("()[]{}")
