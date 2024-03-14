class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        from collections import Counter
        import re

        paragraph = [
            word
            for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]
        result = Counter(paragraph)
        print(result.most_common(1)[0][0])


sol = Solution()
sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
