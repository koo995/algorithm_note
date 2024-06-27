def solution():
    n = int(input())  # 2 이상 10만 이하
    arr = list(map(int, input().split()))
    arr.sort()
    s = 0
    e = 1
    min_diff = int(2e9)
    answer = []
    # 자 여기서 두 용액의 합이 0과 최대한 가까워야 한다. 그 말인 즉슨 abs(0 - (arr[i] + arr[j])) 가 최소값이 되는 지점을 찾으면 된다.
    #  그럴려면... 두개의 합이 최소가 되는 곳을 찾아야 겠구나?가 아니라... 0 에 가까워야 겠네
    # 정렬과 투포인터를 사용하는 이유는 불필요한 경우를 탐색하지 않기 위함이다.
    while 0 <= s < e < n:
        sum_value = arr[s] + arr[e]
        if abs(0 - sum_value) < min_diff:
            min_diff = abs(0 - sum_value)
            answer = [arr[s], arr[e]]
        if sum_value < 0:
            s += 1
            e += 1
        elif sum_value > 0:
            s -= 1
        else:  # s == 0 이라면 정답 그 자체이다
            answer = [arr[s], arr[e]]
            break


    print(*answer)



solution()