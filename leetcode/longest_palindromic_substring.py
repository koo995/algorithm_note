class Solution:
    def longestPalindrome(self, string: str) -> str:
        if len(string) == 1 or string == string[::-1]:
            return string

        def expand(start, end):
            while start >= 0 and end < len(string) and string[start] == string[end]:
                start -= 1
                end += 1
            return string[start + 1 : end]

        result = ""
        for i in range(len(string) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result

    def lpd(self, s: str) -> str:
        # 2개의 2포인터를 쓰면서 확장해 나가는 방식을 사용해보자.
        def expand(start, end):
            while s[start] == [end] and start > 0 and end < len(s):
                start -= 1
                end += 1
            return s[start : end - 1]

        # 투 포인트의 무빙을 어떻게 정의할까
        # 기존에는 슬리이싱 윈도우마냥.. 리스트를 이용하여 움직일수도 있다.
        # 내가 원하는 것은움직여 가면서


sol = Solution()
sol.longestPalindrome("babad")
# 와.... 이건 반드시 따로 다시 풀어보자.
