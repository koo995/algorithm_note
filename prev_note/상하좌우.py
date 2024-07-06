#상하좌우

n = int(input())
plans = input().split()

#LRUD
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
moves = ['L', 'R', 'U', 'D']
loc = [1,1]
nx, ny = 0, 0
for plan in plans:
    for move in moves:
        if plan == move:
            nx = loc[1] + dx[moves.index(move)]
            ny = loc[0] + dy[moves.index(move)]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    loc[1] = nx
    loc[0] = ny
    
print(loc)
        