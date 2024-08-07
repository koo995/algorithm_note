def solution(m, n, board):
    def get_remove_index(b):
        remove_index = set()
        for i in range(len(b) - 1):
            for j in range(len(b[0]) - 1):
                if b[i][j] == '0':
                    continue
                if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1]: # 여기서 심각한 문제가 발생했네... 같은 녀셕을 체크하고 있어...
                    remove_index.add((i, j))
                    remove_index.add((i+1, j))
                    remove_index.add((i, j+1))
                    remove_index.add((i+1, j+1))
        return remove_index
    
    def update(idxs):        
        for y, x in idxs:
            board[y][x] = '0'
        stack = []
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] != '0':
                    stack.append(board[i][j])
            for i in reversed(range(len(board))):
                board[i][j] = stack.pop() if stack else '0'

    board = [list(row) for row in board]
    while 1:
        remove_index = get_remove_index(board)
        if not remove_index:
            break
        update(remove_index)       
    return sum([row.count("0") for row in board])


def solution2(m, n, board):
    def get_remove_points():
        points = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == "":
                    continue
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1]:
                    points |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
        return points

        return new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1]

    new_board = [[board[j][i] for j in reversed(range(m))] for i in range(n)]
    remove_points = set()
    count = 0
    while 1:
        remove_points = get_remove_points()
        if not remove_points:
            break
        count += len(remove_points)
        for remove_point in remove_points:
            i, j = remove_point  # 이 녀석들을 어떻게 제거하지?
            new_board[i][j] = ""
        for i in range(n):
            for j in reversed(range(m)):
                if new_board[i][j] == "":
                    new_board[i].pop(j)
                    new_board[i].append("")
    return count



