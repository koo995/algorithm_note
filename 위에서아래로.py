#위에서 아래로
n = int(input())
array = []
for i in range(n):
    array.append(tuple(input().split()))
    
array.sort(key=lambda student: student[1], reverse=True)
    
print(array)
    
