class Solution:
    def trap(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        after_raining = heights.copy()
        for i in range(n):
            print("i: ", i, "stack: ", stack)
            while stack and heights[stack[-1]] <= heights[i]:
                prev_i = stack.pop()
                while stack and stack[-1] < prev_i or heights[stack[-1]] <= heights[i]:
                    after_raining[prev_i] = heights[stack[-1]]
                    prev_i -= 1
                after_raining[prev_i] = heights[prev_i]
            stack.append(i)
        print("after_raining: ", after_raining)
        trapping_rain_water = 0
        for i in range(n):
            trapping_rain_water += after_raining[i] - heights[i]
        print("trapping_rain_water: ", trapping_rain_water)

    def trap1(self, heights: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(heights)):
            # 변곡점을 만나는 경우
            print("i: ", i, "stack: ", stack)
            while stack and heights[i] > heights[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                if not stack:
                    break
                # distance는 너비
                distance = i - stack[-1] - 1
                # waters는 높이
                waters = min(heights[i], heights[stack[-1]]) - heights[top]
                print("top: ", top, "distance: ", distance, "waters: ", waters)
                volume += distance * waters
            stack.append(i)
        print("volume: ", volume)
        return volume

    def trap2(self, heights):
        if not heights:
            return 0
        volume = 0
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        while left < right:
            left_max, right_max = max(heights[left], left_max), max(heights[right], right_max)
            # 더 높은 쪽을 향해 투포인터 이동
            if left_max <= right_max:
                volume += left_max - heights[left]
                left += 1
            else:
                volume += right_max - heights[right]
                right += 1
        return volume

    def trap3(self, heights: list[int]) -> int:
        # 양 끝은 물이 안차는구나?
        n = len(heights)
        stack = []
        water = 0
        for current_idx in range(n):
            while stack and stack[-1][1] <= heights[current_idx]:
                prev_idx, prev_height = stack.pop()
                if stack:
                    water_height = min(heights[current_idx], stack[-1][1]) - prev_height
                    water_width = current_idx - stack[-1][0] - 1
                    water += water_height * water_width
            stack.append((current_idx, heights[current_idx]))
        return water


sol = Solution()
sol.trap1([4, 2, 0, 3, 2, 5])
# [0, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 1]
