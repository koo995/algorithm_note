def get_zero_count(y, x):
    count = 0
    for i in range(9):
        if i == y:
            continue
        if table[i][x] == 0:
            count += 1
    for i in range(9):
        if i == x:
            continue
        if table[y][i] == 0:
            count += 1
    # 속한 네모모양 칸에 0이 있는지 살펴보자.
    middle_y, middle_x = 3 * (y // 3) + 1, 3 * (x // 3) + 1
    for i in range(8):
        if y == middle_y + d_y[i] and x == middle_x + d_x[i]:
            continue
        if table[middle_y + d_y[i]][middle_x + d_x[i]] == 0:
            count += 1
    return count

def check(y, x, num):
    for i in range(9):
        if x == i:
            continue
        if table[y][i] == num:
            return False
    for i in range(9):
        if y == i:
            continue
        if table[i][x] == num:
            return False
    middle_y, middle_x = 3 * (y // 3) + 1, 3 * (x // 3) + 1
    for i in range(9):
        if y == middle_y + d_y[i] and x == middle_x + d_x[i]:
            continue
        if table[middle_y + d_y[i]][middle_x + d_x[i]] == num:
            return False
    return True

def sudoku(n):
    if n == len(zero_points):
        for row in table:
            print(*row)
        exit() # 여기서 exit 하지 않으면.. 함수 빠져 나오고 다시 탐색이 이루어지는데... 
    for num in range(1, 10):
        y, x, _ = zero_points[n]
        if check(y, x, num):
            table[y][x] = num
            sudoku(n + 1)
            table[y][x] = 0
        
    
table = [list(map(int, input().split())) for _ in range(9)]
d_y = [0, -1, -1, 0, 1, 1, 1, 0, -1]
d_x = [0, 0, 1, 1, 1, 0, -1, -1, -1]
zero_points = []
for y, row in enumerate(table):
    for x, num in enumerate(row):
        if num != 0:
            continue
        # 여기서 후보가 몇개가 가능한지 함께 기록하자.
        count = get_zero_count(y, x)
        zero_points.append((y, x, count))
zero_points.sort(key=lambda point:point[2])
sudoku(0) # 이 녀석과 퀸 문제와 비슷한 것을 볼수있어야하는데...
