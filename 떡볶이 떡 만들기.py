n, m = map(int, input().split())
array = list(map(int, input().split()))

def cutting(array, height):
    result = 0
    for i in array:
        if i > height:
            result += i - height
    return result
            
def binary_search(array, s, e):
    global start
    global end
    global result
    start = s
    end = e
    mid = (start + end) // 2
    print("현재 길이: ", mid)
    if start > end:
        return None
    else :
        if cutting(array, mid) >= m:
            #우선 결과를 만족한다면 그 값을 저장해 준다.
            # 그리고 이진 탐색을 한번더 수행!
            # 한번더 수행되었을때 결과가 만족할 수도 있고 아닐수도 있으니 변수에 값을 저장해 두는 방식은 유용할듯
            result = mid 
            return binary_search(array, mid+1, end)
        elif cutting(array, mid) < m:
            return binary_search(array, start, mid-1)

start = 0
end = max(array)
result = 0
binary_search(array, start, end)
print(result)

# 이번에도 무한 재귀함수 루프가 나왔다. 종료조건을 명시해야 할듯
# 최대값이란 말이지 일치하는 경우를 찾는 것이 아니야. 답안에서는 result의 변수를 하나를 둬서 처리하네... 함수에서 반환받는 방식은 최대 최소를 처리하기에 무리가 있는 걸까?
# 발견을 하긴 했다. 함수에 초기값으로 설정을 했더니 start와 end가 바뀌었는데도 그걸 반영하지 못하였네