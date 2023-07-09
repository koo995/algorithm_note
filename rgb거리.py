import copy

n = int(input())
# 테이블값을 초기화 함.
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))
print(table)

result = [[]*3 for _ in range(n)]
result[0] = table[0]
print(result)
for i in range(1, n):
    for j in range(3):
        prev_t = copy.deepcopy(result[i-1])
        prev_t.pop(j)
        result[i].append(min(prev_t) + table[i][j])
print(min(result[n-1]))
    
