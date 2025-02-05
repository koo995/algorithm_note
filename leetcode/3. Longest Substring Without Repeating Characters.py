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

    # 다른사람 풀이
    def lengthOfLongestSubstring2(self, array: str) -> int:
        # 어떻게 해결할까? 새롭게 탐색하는 녀석.. set 자료구조를 이용하면 될듯?
        from collections import deque
        start = 0
        dic = {}  # 여기다가는 해당 문자의 인덱스를 저장한다.
        n = len(array)
        result = 0
        for end in range(n):
            if array[end] in dic and dic[array[end]] >= start:
                start = dic[array[end]] + 1
            dic[array[end]] = end
            result = max(result, end - start + 1)
        return result

    def lengthOfLongestSubstring3(self, array: str) -> int:
        # 어떻게 해결할까? 새롭게 탐색하는 녀석.. set 자료구조를 이용하면 될듯?
        from collections import deque
        q = deque()
        result = 0
        for ch in array:
            while ch in q:
                q.popleft()
            q.append(ch)
            result = max(result, len(q))
        return result

    def lengthOfLongestSubstring4(self, s: str) -> int:
        # 아하 연속된 녀석이어야 하구나?
        # 그리고 모든 녀석이 나타날 필요는 없구나?
        from collections import deque

        q = deque()
        seen = set()
        answer = 0
        for ch in s:
            while ch in seen:
                prev = q.popleft()
                seen.remove(prev)

            q.append(ch)
            seen.add(ch)
            answer = max(answer, len(q))
        return answer


sol = Solution()
sol.lengthOfLongestSubstring("pwwkew")
sol.lengthOfLongestSubstring("au")
sol.lengthOfLongestSubstring("dvdf")