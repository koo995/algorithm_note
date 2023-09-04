N = int(input()) # 1~1e6
arr = list(map(int, input().split())) # 각 원소의 크기도 100만 까지
    
for idx, element in enumerate(arr):
    def NGE(e, r_arr):
        # 본인 포함 길이가 1인 경우는 존재하지 않겠지
        if len(r_arr) == 1:
            return -1
        result = -1
        for i in r_arr:
            if e < i:
                result = i
                break
        return result
    
    result = NGE(element, arr[idx:])
    print(result, end=' ')
    
# 오큰수를 어떻게 구할까?
# 시간 초과가 발생했다.