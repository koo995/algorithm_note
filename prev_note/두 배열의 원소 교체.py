#두 배열의 원소 교체
n, k = map(int,input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

sorted_a = sorted(array_a)
sorted_b = sorted(array_b, reverse=True)
for i in range(k):
    sorted_a[i] = sorted_b[i]
    
sum = 0
for i in range(len(sorted_a)):
    sum += sorted_a[i]

print(sum)