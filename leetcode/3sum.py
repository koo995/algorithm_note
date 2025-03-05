class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print("nums: ", nums)
        three_sum_lst = []
        # i 앞에 기본적으로 2개의 포인터가 더 있으니 2개 앞까지만 간다.
        for i in range(len(nums) - 2):
            # 중복된 연산을 없애기 위함
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while i < left < right:
                print("i: ", i, "left: ", left, "right: ", right)
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    three_sum_lst.append((nums[i], nums[left], nums[right]))
                    # 여기에서 중복을 피하기 위함이라...
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return three_sum_lst
sol = Solution()
sol.threeSum([-1, 0, 1, 2, -1, -4])
sol.threeSum([-2, 0, 0, 2, 2])

# 3개의 수의 합이 0을 이루는 모든 경우의수를 구하는 것이 문제이다.
# 단순히 모든케이스를 확인하는 것은 중복되는 연산이 발생한다.
# 모든 조합을 찾아볼까? 그렇지만
# 흠... 시간초과가 걸렸다.
# 중복되는 것 때문인데.. i와 left가 붙어있는데... 여기서 같은 값일 확률이 올라간다. 정렬을 했은까
# 이 중복되는 문제를 어떻게 처리하지...? 인덱스는 다르지만 값은 같은 경우다. set으로 하기에는 시간초과가 발생한다.
# 두번째 케이스에서 또 중복이 발생한다...

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        results = []

        for i in range(N - 2):
            # (1) 중복 체크: i > 0이고 현재 값이 이전 값과 같다면 스킵
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # (2) 조기 종료 조건
            # nums[i]가 양수이면, 뒤에 있는 모든 값도 >= nums[i]이므로 합이 0을 만들 수 없음
            if nums[i] > 0:
                break

            # 가장 큰 두 수(nums[-1], nums[-2])와의 합이 여전히 0보다 작으면
            # i번째 값이 너무 작다는 의미이므로 다음 i로 넘어가도 됨
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue

            left, right = i + 1, N - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # (3) 중복 스킵
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return results
