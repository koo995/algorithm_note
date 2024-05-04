def solution():
    def get_similar_num_index(num) -> int:
        # num 보다 조금 더 큰녀석을 찾는다...
        s = 0
        e = len(lis) -1
        while s < e:
            m = (s + e) // 2
            if num <= lis[m]:
                e = m
            else:
                s = m + 1 # 이 부분이 중요하다. 
        return e # 반환값이 e 인 것도 중요하다.
    
    
    N = int(input())
    arrays = list(map(int, input().split()))
    lis = [arrays[0]]
    for num in arrays[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            # 작다면... num과 가장 차이가 안나면서 더 큰 원소를 찾는다?
            idx = get_similar_num_index(num)
            lis[idx] = num
    print(len(lis))

solution()
# 자... 구현은 얼핏하긴했는데... 논리적인 이유부터 찾아보자