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


def solution2():
    def find_greater_idx(n):
        s = -1
        e = len(lis)
        while s + 1 < e:
            m = (s + e) // 2
            if lis[m] <= n:
                s = m
            else:
                e = m
        return e

    N = int(input())
    array = list(map(int, input().split()))
    lis = [array[0]]
    # 가장 긴 증가하는 수열을 찾아야한다.
    if N == 1:
        print(1)
        return
    for i in range(1, N):
        if lis[-1] < array[i]:
            lis.append(array[i])
        else: # 만약에 같거나 더 작다면...? 어떤 값과 바꿔치기해서... 증가하는 수열로 만들면 되게 좋겠다. 그러면 누구랑 바꿀까?
            idx = find_greater_idx(array[i])
            lis[idx] = array[i]

    print(len(lis))


solution2()
# 자... 구현은 얼핏하긴했는데... 논리적인 이유부터 찾아보자