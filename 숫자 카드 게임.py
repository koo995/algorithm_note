#숫자 카드 게임
n, m = map(int, input().split())
INF = 1e9
array = [[] for _ in range(n)]
result = -INF
for i in range(n):
    array[i] = list(map(int, input().split()))
    min_value = min(array[i]) #최소값을 찾느것은 이 라이브러리를 이용하자. sort후에 가장 앞에 있는것은 별로인가
    if (min_value > result):
        result = min_value

print(result)

#참고
n = 3
array = [[] * n]
print(array)  # Output: []

array[0].append(1)
print(array)  # Output: [1]

array[1].append(2)
print(array)  # Output: [1, 2]
