class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # nums을 입력받으면 가능한 모든 순열를 리턴해라 즉 순서가 있다.
        # 사실 itertools 을 쓰면 가능하긴한데... 그걸 제외하고 풀어보자.
        def dfs(left_nums, path):
            if len(path) == len(nums):
                result.append(path)
                return 
            for idx, num in enumerate(left_nums):
                next_path = path.copy()
                next_path.append(num)
                next_left_nums = left_nums.copy()
                next_left_nums.pop(idx)
                dfs(next_left_nums, next_path)
                
        result = []
        dfs(nums, [])
        return result
    
    def permute2(self, nums: list[int]) -> list[list[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return results
                
    
    
sol = Solution()
sol.permute([1,2,3])


    