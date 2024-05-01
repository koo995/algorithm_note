class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i:i[0])
        # 겹친다는 것이 뒷녀석의 앞부분이 현녀석의 뒷부분보다 크거나 같은 경우다.
        merged_intervals = [intervals[0]] # 그런데 꼭 2개만 겹쳐야한다는 보장은 없잖아? 3개가 겹칠수 있지 않나?
        for idx, intvl in enumerate(intervals[1:]):
            start, end = intvl
            pre_start, pre_end = merged_intervals[-1]
            if pre_end < start:
                merged_intervals.append(intvl)
                continue
            if start <= pre_end and end <= pre_end:
                intvl = [pre_start, pre_end]
            elif start <= pre_end:
                intvl = [pre_start, end]
            merged_intervals[-1] = intvl
            
        return merged_intervals
            
    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x:x[0]):
            print(i)
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i, # 여기 이 콤마 뭐야...
        return merged

sol = Solution()
sol.merge2([[1,3],[2,6],[8,10],[15,18]])