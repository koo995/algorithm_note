n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
    
array.sort()
print(array)

data = [-1] * (10000+1)

for i in array:
    data[i] = 1
    
for i in range(array[0]+1,m+1):
    list = [data[i-j]+1 for j in array if i-j > 0 and data[i-j]>0 ]
    list.sort()
    if list:
        data[i] = list[0]

print(data[m])

# 어떤 알고리즘을 써야할지 잘 모르겠어. 이게 진짜 dp야?
# 동전보다 큰 녀석은 data[i] = min([data[i-j]+1 for j in array]) 이걸로 처리하면 될거 같은데
# 그 사이에 녀석들도 몇몇 조건 추가하니 가능은 하네...
# 그 사이에 있는 녀석들은 어떻게 해야하나?
# 리스트안에 무언가가 비엇다는 것은 조건이 안되나?
# 빈 리스트는 그 자체로 False값을 가지는구나
