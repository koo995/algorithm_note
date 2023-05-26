n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
request = list(map(int, input().split()))


def binary_search(target, start = 0, end = len(array)-1):
    if start >= end:
        return print('no', end =' ')
    else:
        mid = (start+end) // 2
        if target == array[mid]:
            return print("yes", end = ' ')
        elif target < array[mid]:
            return binary_search(target, end = mid-1)
        else :
            return binary_search(target, start = mid+1)
    #모든 조건을 if로 설정하고 마지막에 return print('no')는 출력이 안됨... 이미 앞에서 다 걸러졌기 때문?


for item in request:
    binary_search(item)
    
    
# 재귀함수가 무한으로 호출되는 문제 발생 재귀함수가 종료될 "조건"을 명시해 줘야지 어떤 상황일때 return none이라는?
# # 그 조건은 end가 start보다 작아지는 경우구나...
# 근데 그 경우에 없다고 출력을 해야하는 것인가...
# 원래는 if 문 3개를 하고 마지막에 return을 했는데 no가 출력이 안되었지...
# 중요한거 까먹었네... array가 정렬되어있어야 하는데 sort을 안했었어
# 집합 자료형을 사용하는 방법도 좋구나? 시간복잡도에 큰 영향을 안미치나? if i i array 이 조건말야