class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        num_count = Counter(nums).items()
        sorted_count = sorted(num_count, key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_count[:k]]


sol = Solution()
sol.topKFrequent([1,1,1,2,2,3], 2)