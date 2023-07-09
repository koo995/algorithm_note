t = int(input())
values = []
for _ in range(t):
    values.append(int(input()))

fibo= [0] * 41
fibo[0] = 0
fibo[1] = 1
zero_table = [0] * 41
zero_table[0] = 1
zero_table[1] = 0
one_table = [0] * 41
one_table[0] = 0
one_table[1] = 1

for i in range(2, 41):
    fibo[i] = fibo[i-1] + fibo[i-2]
    zero_table[i] = zero_table[i-1] + zero_table[i-2]
    one_table[i] = one_table[i-1] + one_table[i-2]
    
for v in values:
    print(zero_table[v], one_table[v])
 
 
# 밑의 방식은 표를 그려보니 왜 그런지는 알겠지만.. 무슨 원리인지는 잘 모르겠다
for i in range(int(input())):
    a, b = 1, 0
    for _ in range(int(input())):
        a, b = b, a + b
    print(a, b)
