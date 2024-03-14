class Solution:
    def reverseString(self, s: list[str]) -> None:
        s = s[::-1]
        print("s: ", s)


sol = Solution()
sol.reverseString(["h", "e", "l", "l", "o"])
