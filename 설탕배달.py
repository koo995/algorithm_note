n = int(input())
table = [1e4] * (n+3) # 어짜피 n은 5000까지고 3으로 다 나눠도 천몇백이 최대다
table[3] = 1
table[5] = 1
for i in range(1, n+1): # 아하 여기서 4가 들어가면 6,5 니까 문제가 발생하네
    if i < 6:
        continue
    min_v = min(table[i-3] +1 , table[i-5] + 1) # 한녀석은 -1이고 다른 녀석은 그보다 클 수 있는데 min을 사용하기에는 음...
    table[i] = min_v
if table[n] >= int(1e4):
    print(-1)
else:
    print(table[n])

# 봉지는 3키로 5키로
# 최대한 적은 봉지를 들고 간다.
# 5이하는 그냥 무시하는게 깔끔하네 