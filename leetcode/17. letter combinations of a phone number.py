class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        def dfs(left_digits, s) -> None:
            # 더이상 숫자가 없으면 끝낸다.
            if not left_digits:
                answer.append(s)
                return
            for ch in keypad[left_digits[0]]:
                dfs(left_digits[1:] if len(left_digits) > 1 else "", s + ch)
        
        # digits의 최대는 4 최소는 0
        # 기본적으로 숫자에 어떤 값이 매핑되어있는지 dic을 정할 필요가있을것 같다.
        keypad = {"2":("a", "b", "c"), "3":("d", "e", "f"), "4":("g", "h", "i"),
                  "5":("j", "k", "l"), "6":("m","n","o"), "7":("p", "q", "r", "s"),
                  "8":("t", "u", "v"), "9":("w", "x", "y", "z")}
        # 결국엔 완전탐색이 아닌가?
        answer = []
        # digits 을 하나하나 먼저 시작하면서 모든 가지들을 다 탐색해 나가야 한다.
        if not digits:
            return []
        dfs(digits, "")
        return answer
    
    def letterCombinations2(self, digits: str) -> list[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)
        
        if not digits:
            return []
        
        dic = {"2":("a", "b", "c"), "3":("d", "e", "f"), "4":("g", "h", "i"),
                  "5":("j", "k", "l"), "6":("m","n","o"), "7":("p", "q", "r", "s"),
                  "8":("t", "u", "v"), "9":("w", "x", "y", "z")}
        result = []
        dfs(0, "") # 그렇지 이런 방법도 있었어... 지니가는 길을 기록해 나가는 방법이지
    
sol = Solution()
sol.letterCombinations("23")