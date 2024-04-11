class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(current_candidate, path, csum):
            # 매번 합을 더해나가는 것이 아무래도 연산량이 좀더 소모된다.
            # 그래서 합을 따로 기록해 나갔다.
            if csum >= target:
                if csum == target:
                    result.append(path)
                return
            for idx, num in enumerate(current_candidate):
                n_path = path.copy()
                n_path.append(num)
                dfs(current_candidate[idx:], n_path, csum + num)
            
        candidates.sort()
        result = []
        dfs(candidates, [], 0)
        return result
    
    # 이게 더 빠르네... 역시
    def combinationSu2m(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
        result = []
        dfs(target, 0, [])
        return result

    
    
    
sol = Solution()
sol.combinationSum([2,3,6,7], 8)