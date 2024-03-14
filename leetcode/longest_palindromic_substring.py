class Solution:
    def longestPalindrome(self, string: str) -> str:
        if len(string) == 1 or string == string[::-1]:
            return string

        def expand(start, end):
            while start > 0 and end < len(string) and string[start] == string[end]:
                start -= 1
                end += 1
            return string[start + 1 : end]

        result = ""
        for i in range(len(string) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


sol = Solution()
sol.longestPalindrome("babad")
# 와.... 이건 반드시 따로 다시 풀어보자.
