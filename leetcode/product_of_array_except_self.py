class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_product = 1
        left_out = []
        for i in range(n):
            left_out.append(left_product)
            left_product *= nums[i]
        print("left_out: ", left_out)
        right_product = 1
        right_out = []
        # 여기서 거꾸로 탐색이 이루어지는 것은 어떻게 하지?
        for i in range(n - 1, -1, -1):
            right_out.append(right_product)
            right_product *= nums[i]
        right_out = right_out[::-1]
        print("right_out: ", right_out)
        total_out = []
        for i in range(n):
            total_out.append(left_out[i] * right_out[i])
        print("total_out: ", total_out)

    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_product = 1
        out = []
        for i in range(n):
            out.append(left_product)
            left_product *= nums[i]
        right_product = 1
        # 여기서 거꾸로 탐색이 이루어지는 것은 어떻게 하지?
        for i in range(n - 1, -1, -1):
            out[i] *= right_product
            right_product *= nums[i]
        print("out: ", out)
        return out

sol = Solution()
sol.productExceptSelf1([1,2,3,4])
# 주의해야 할 것은.. 중간에 0이 끼워져 있을 수 있다는 것이다.
# 그리고 0을 곱해야 하는 경우가 있을 수 있다는 것이다.
# 왼쪽의 곱셈 결과를 모두 구해놓고... 오늘쪽 곱셈 결과를 곱해준다?