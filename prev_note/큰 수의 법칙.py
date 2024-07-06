#큰 수의 법칙
n, m, k = map(int, input().split()) #m번 더하고 k번 반복 가능 배열의 크기는 n
array = list(map(int,input().split()))

array.sort(reverse=True)
result = 0
cnt = 0
while(cnt < m):
    for _ in range(k):
        result += array[0]
        cnt +=1
    result += array[1]
    cnt +=1
    
print(result)