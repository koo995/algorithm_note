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


class Solution:
    def longestPalindrome(self, string: str) -> str:
        def get_odd_palind(i):
            s = i
            e = i + 1
            if not (0 <= s < e < n and string[s] == string[e]):
                return string[s]
            while 0 <= s < e < n and string[s] == string[e]:
                s -= 1
                e += 1
            return string[s+1:e]

        def get_even_palind(i):
            s = i - 1
            e = i + 1
            if not (0 <= s < e < n and string[s] == string[e]):
                return string[i]
            while 0 <= s < e < n and string[s] == string[e]:
                s -= 1
                e += 1
            return string[s+1:e]
        # 앞에서 탐색하나 뒤에서 탐색하나 같아야한다.
        n = len(string)
        results = []
        for idx in range(n):
            results.append(get_odd_palind(idx))
            results.append(get_even_palind(idx))
        results.sort(key=lambda result:len(result), reverse=True)
        return results[0]


class Solution2:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        max_value = ""

        for i in range(len(s)):
            start = i
            end = i
            start2 = i
            end2 = i + 1
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    max_value = s[start:end + 1]
                start -= 1
                end += 1

            while 0 <= start2 and end2 < len(s) and s[start2] == s[end2]:
                if end2 - start2 + 1 > max_len:
                    max_len = end2 - start2 + 1
                    max_value = s[start2:end2 + 1]
                start2 -= 1
                end2 += 1
        return max_value


