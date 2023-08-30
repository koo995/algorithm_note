# import copy

# n = int(input())
# arr = list(map(int,input().split()))
# min_points = [arr.index(a) for a in arr if a < 0] # 음수인 녀석들 다 찾는다.
# sums = [[0] * n for _ in range(len(min_points))]
# # 이제부터 dp시작.
# max_value = -1
# if n == 1:
#     print(arr[0])
# else :
#     if min_points:
#         for idx, min_p in enumerate(min_points):
#             temp_arr = copy.deepcopy(arr)
#             temp_arr.pop(min_p)
#             sums[idx][0] = temp_arr[0]
#             for i in range(1, n-1):
#                 sums[idx][i] = max(sums[idx][i-1] + temp_arr[i], temp_arr[i-1] + temp_arr[i], temp_arr[i])
#                 if max_value < sums[idx][i]:
#                     max_value = sums[idx][i]
#     else:
#         print(sum(arr))
# print(sums)
# print(max_value)
        
            
# 단순히 제일 작은 음수를 제거한다는게 의미가 있을까?
# 메모리 초과가 발생...


import copy

n = int(input())
arr = list(map(int,input().split()))
min_points = [arr.index(a) for a in arr if a < 0] # 음수인 녀석들 다 찾는다.
# 이제부터 dp시작.
max_value = -1
if n == 1:
    print(arr[0])
else :
    if min_points:
        for min_p in min_points:
            sums = [0] * n
            temp_arr = copy.deepcopy(arr)
            temp_arr.pop(min_p)
            sums[0] = temp_arr[0]
            for i in range(1, n-1):
                sums[i] = max(sums[i-1] + temp_arr[i], temp_arr[i-1] + temp_arr[i], temp_arr[i])
                if max_value < sums[i]:
                    max_value = sums[i]
    else:
        print(sum(arr))
print(max_value)
# 하긴... 음수가 100개만 넘어가도 말이 안되는 것이네...
