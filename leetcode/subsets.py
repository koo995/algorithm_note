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
    
sol = Solution()
sol.subsets([1,2,3])
# 중복된 데이터가 들어가는데...