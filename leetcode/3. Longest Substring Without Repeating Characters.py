class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        # 중복 문자가 없는 가장 긴 문자열의 길이를 반환하. 각 케이스가 아니라 길이만 반환하면 되는구나?
        # 해시라는 딕을 만들고 계속해서 입력으로 넣다가... 중복되는 녀석이 발생하면 그 녀석부터 다시 넣는다?
        start = 0
        end = 0
        max_len = 0
        while start <= end < len(s):
            # 없으면 갱신하고 있으면 없을때까지 start을 늘린다.
            while s[end] in s[start:end]:
                start += 1
            max_len = max(max_len, end - start + 1)
            end += 1
        print(max_len)


sol = Solution()
sol.lengthOfLongestSubstring("pwwkew")
sol.lengthOfLongestSubstring("au")
sol.lengthOfLongestSubstring("dvdf")