class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict

        jewels_dic = defaultdict(int)
        for jewel in jewels:
            jewels_dic[jewel] = 0
        for stone in stones:
            if stone in jewels_dic:
                jewels_dic[stone] += 1
        return sum(jewels_dic.values())
