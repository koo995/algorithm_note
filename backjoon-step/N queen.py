# n = int(input())

# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
    
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         return

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다. 이걸 이렇게 표현할 수 있다니...
#             # 아니 근데.. 여기 이렇게 놓겠다가 되었으면.. 롤백도 해야하지 않나? 아... 위협을 받는다면 계속해서 i 값으로 업데이트 되는 구나?
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)




N = int(input())
count = 0
row = [0] * N

def is_under_attack(y):
    for prev_y in range(y): # x 값보다 작은 y값만 보면 된다.
        # 다른 row 에 x의 값을 가지고 있다면 안되고.. 대각선도 안됨
        if row[prev_y] == row[y] or y - prev_y == abs(row[prev_y] - row[y]):
            return True
    return False

def n_queens(y):
    global count
    
    if y == N: # 한발짝 더 나아갔다가 리턴하는 것이다.. 
        count += 1
        return # 여기서 더이상 탐색하지 말아야 한다...
    
    for x in range(N):
        row[y] = x
        if is_under_attack(y):
            continue
        n_queens(y + 1)
            
n_queens(0)
print(count)