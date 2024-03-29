class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # temperatures 는 최대 10만까지
        stack = []
        waiting_day = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            # 스택의 제일 위에 있는 녀석보다 temp 가 크다면 역으로 탐색해 나간다.
            while stack and temperatures[stack[-1]] < temp:
                top_idx = stack.pop()
                waiting_day[top_idx] = idx - top_idx
            stack.append(idx)
        print("waiting_day", waiting_day)

sol = Solution()
sol.dailyTemperatures([73,74,75,71,69,72,76,73])