class Solution:

    def arrayPairSum(self, nums: list[int]) -> int:
        def generator_of_even():
            even_num: int = 0
            while even_num < len(nums):
                yield even_num
                even_num += 2

        nums.sort()
        maximized_sum = 0
        for i in generator_of_even():
            maximized_sum += min(nums[i], nums[i + 1])
        print("max: ", maximized_sum)
        return maximized_sum


sol = Solution()
sol.arrayPairSum([1, 4, 3, 2])
