class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        result = []
        dfs(0, [])
        return result
    
    
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        def dfs(cnums, path:list):
            if not cnums:
                results.append(path)
                return
            n_path = path.copy()
            dfs(cnums[1:] if len(cnums) > 1 else [], n_path)
            n_path.append(cnums[0])
            dfs(cnums[1:] if len(cnums) > 1 else [], n_path)
        results = []
        dfs(nums, [])
        return results

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        answers = [[]]

        # 여기서 모든 집합을 어떻게 구해야할까?
        # 단순히 라이브러리를 사용하는 것이 아니라... 음... 있고 없고를 탐색해야겠는데?
        def dfs(start, path):
            answers.append(path)
            if start == N - 1:
                return

            # 현재 탐색한 곳에서 기록을 이어간다.

            for n_i in range(start, N):
                # start번째를 이미 넣었으니까 그 다음부터 탐색한다.
                if n_i == start:
                    continue
                dfs(n_i, path + [nums[n_i]])

        N = len(nums)
        for i in range(N):
            # 여기서 탐색을 하면..
            # i번째 녀셕이 포함된 집합들을 탐색하는 것이다.
            dfs(i, [nums[i]])
        return answers
    
sol = Solution()
sol.subsets([1,2,3])
# 중복된 데이터가 들어가는데...