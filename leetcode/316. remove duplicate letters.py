import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        print("set(s): ", set(s))
        # 집합으로 정렬
        for char in sorted(set(s)):
            print("char: ", char)
            suffix = s[s.index(char):]
            print("suffix: ", suffix)
            # suffix의 문자열에 해당하는 녀석들이 모든 원소를 다 가지고 있는 경우라면...
            if set(s) == set(suffix):
                print("if 조건 만족")
                result = char + self.removeDuplicateLetters(suffix.replace(char, ''))
                print("result: ", result)
                return result
        print("for 문 끝")
        return ''

    def removeDuplicateLetters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return "".join(stack)


# 문제 이해가 쉽지 않다. 하지만 상당히 흥미롭다...
"""
There a many people confused in the comments. if you are one of the them then this comment is for you.
The goal of this problem is to find a string answer that satisfies these conditions:

the answer must contains all the letters that are there in the original string s.
the answer must not have any duplicate character.
the answer must be a subsequence of the original string s.
in case multiple strings pass the above 3 conditions, return the one which is lexicographically smallest.
"""


sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")