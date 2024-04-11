class Solution:
    # 이 방식 상당히 느리네... itertools가 엄청나게 빠르구나?
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(remain_lst, path):
            # 먼저 첫번째 녀석을 넣는다.
            # 그리고 나머지 녀석들을 차례로 넣는다. 
            if len(path) == k:
                result.append(path)
                return
            for idx, num in enumerate(remain_lst):
                n_path = path.copy()
                n_path.append(num)                
                dfs(remain_lst[idx+1:] if idx + 1 < len(remain_lst) else [], n_path)


        
        lst = [i for i in range(1, n+1)] # [1,2,3,4,5] 라 했을때... 모든 경우를 따져가며 어쨋든 완전탐색인가?
        # lst에서 k개의 원소를 가지는 조합을 찾자
        result = []
        dfs(lst, [])
        print("result: ", result)
        return result
    
sol = Solution()
sol.combine(4, 2)

