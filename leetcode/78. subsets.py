class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(status, path):
            results.append(path)
            for i in range(n):
                n_status = status | 1 << i
                if visited[n_status] == 1:
                    continue
                visited[n_status] = 1
                n_path = path.copy()
                n_path.append(nums[i])
                dfs(n_status, n_path)

        n = len(nums)
        results = []
        visited = [0] * (1 << n)
        dfs(0b0, [])
        return results

    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result