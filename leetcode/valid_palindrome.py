class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 불필요한 것들은 제거한다.
        stack = []
        s_lower = ""
        for ch in s:
            if ch.isnumeric() or ch.isalpha():
                s_lower += ch.lower()
                stack.append(ch.lower())
        return s_lower == s_lower[::-1]
        # 어떤 자료구조를 쓸까 생각해봤는데 스택을 쓰면 후입선출이니 결과가 같다면 트루를 반환한다.


sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
