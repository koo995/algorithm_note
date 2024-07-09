# Check if there is a winning row, column, or diagonal
def check_win(player, board):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def solution(board):
    num_x = sum(row.count("X") for row in board)
    num_o = sum(row.count("O") for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0

    elif (check_win("O", board) and num_x != num_o - 1) or (
        check_win("X", board) and num_x != num_o
    ):
        return 0

    return 1


def solution3(board):
    # 규칙을 지키더라도 나오면 안되는 경우는
    # x가 더 많으면 탈락
    # o와 x가 같은경우? o의 승리로 게임이 끝난 상태라면 탈락
    # o가 더 많다면? x의 승리로 게임이 끝났는데, o가 놓여짐
    o_count = 0
    x_count = 0
    # 돌들의 갯수를 세어본다.
    for row in board:
        for stone in row:
            if stone == "O":
                o_count += 1
            elif stone == "X":
                x_count += 1
    o_bingo = False
    x_bingo = False
    # 빙고를 확인한다.
    # 대각선을 먼저 확인한다.
    if all(board[i][i] == "O" for i in range(3)):
        o_bingo = True
    if all(board[i][i] == "X" for i in range(3)):
        x_bingo = True
    if all(board[i][2 - i] == "O" for i in range(3)):
        o_bingo = True
    if all(board[i][2 - i] == "X" for i in range(3)):
        x_bingo = True

    for i in range(3):
        if (board[i] == "OOO") \
                or (board[0][i] == board[1][i] == board[2][i] == "O"):
            o_bingo = True
        elif (board[i] == "XXX") \
                or (board[0][i] == board[1][i] == board[2][i] == "X"):
            x_bingo = True
    if x_count > o_count or (o_count - x_count > 1):
        return 0
    elif x_count == o_count and o_bingo == True:
        return 0
    elif x_count < o_count and x_bingo == True:
        return 0
    elif o_bingo == True and x_bingo == True:
        return 0
    return 1

# 이런 풀이도 있구나?
# 케이스를 나누고 행 열 대각선 방향으로 승패 체크하는 것도 알게되었어
# 그렇지만 저 all이란 메서드는 처음보는군
