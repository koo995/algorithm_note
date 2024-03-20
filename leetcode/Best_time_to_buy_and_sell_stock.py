class Solution:
    def maxProfit1(self, prices: list[int]) -> int:
        n = len(prices)
        s = 0
        e = n - 1
        min_value = int(1e9)
        max_value = -int(1e9)
        while s < e:
            # s값이 증가해 나가면서 가장 값이 작은 녀석의 인덱스를 기록한다.
            if prices[s] < max_value:
                min_value = min(prices[s], min_value)
                s += 1
            if prices[e] > max_value:
                max_value = max(max_value, prices[e])
                e -= 1
        print("min_value: ", min_value)
        print("max_value: ", max_value)
        # 현재 이방식에서는... 무한 루프가 발생한다.
        return max_value - min_value if max_value - min_value >= 0 else 0

    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = int(1e9)
        for price in prices:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)
        return profit


sol = Solution()
sol.maxProfit([7,6,4,3,1])
# 각자 조건에 맞게 좁혀져야 한다... 동시에 좁혀지면 답이 안나온다.
