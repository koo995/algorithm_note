# 1이 될때 까지
n, k = map(int, input().split())

result = 0

while( n != 1):
    if(n % k == 0):
        n = n//k
        result += 1
    else:
        n -= 1
        result += 1

print(result)

# n이 k보다 작을때(더 이상 나눌 수 없을때) 반복문을 탈출하도록 바꿔야 할까...
#그리고 효율적으로 한번에 1을 여러번 빼는 방법이 있어