def catch_shark(fisher):
    result = 0
    for i in range(R + 1):
        if shark_board[i][fisher] and shark_board[i][fisher][0] > 0:
            result = shark_board[i][fisher][0]
            # 잡았으니까 각 값을 제거해주는 것이 맞다.
            shark_board[i][fisher].remove(result)
            del shark_point[result]
            return result
    return result

def change_direction(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3

def move(sha, spe):
    y, x = shark_point[sha]

    # 기존의 위치에서 제거한다.
    shark_board[y][x].remove(sha)

    while spe > 0:
        d = shark_direction[sha]
        dy, dx = directions[d]
        n_y = y + dy
        n_x = x + dx
        if not 1 <= n_y <= R:
            # 여기서... 방향이 바뀌어야하구나?
            n_d = change_direction(d)
            shark_direction[sha] = n_d
            continue
        if not 1 <= n_x <= C:
            n_d = change_direction(d)
            shark_direction[sha] = n_d
            continue
        y = n_y
        x = n_x
        spe -= 1
    # 자 이제 거리 이동은 다 했으니까...
    # 옮긴 자리를 체크해줘야한다.
    shark_point[sha] = [y, x]
    shark_board[y][x].append(sha)

def remove_double():
    for i in range(R + 1):
        for j in range(C + 1):
            if len(shark_board[i][j]) > 1:
                shark_board[i][j].sort(reverse = True)
                while len(shark_board[i][j]) > 1:
                    small_shark = shark_board[i][j].pop()
                    # 이제 이 녀석의 정보를 제거해야한다.
                    del shark_point[small_shark]

R, C, M = map(int, input().split())
shark_info = [map(int, input().split()) for _ in range(M)]

directions = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

# 각 상어는 크기로 구분하자
shark_direction, shark_point, shark_speed = {}, {}, {}
shark_board = [[[] for _ in range(C + 1)] for _ in range(R + 1)] # 각 좌표에 상어식별값(사이즈)가 저장되어 있다.
# 이 모든 것을 board을 만들고 체크할 필요가 있을까? 흠... 그냥... 좌표 x 좌표만 탐색하면 되지 않나?
for r, c, s, d, size in shark_info:
    shark_direction[size] = d
    shark_speed[size] = s
    shark_point[size] = [r, c]
    shark_board[r][c].append(size)

total_shark, fisher_point = 0, 0
for _ in range(C):
    fisher_point += 1
    total_shark += catch_shark(fisher_point)
    for shark in shark_point.keys():
        speed= shark_speed[shark]
        move(shark, speed) # 한가지 주의할 점이 같은 칸에 있으면 작은 녀석은 사라진다.
    remove_double()

print(total_shark)