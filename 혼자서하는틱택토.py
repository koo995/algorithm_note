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


# 이런 풀이도 있구나?
# 케이스를 나누고 행 열 대각선 방향으로 승패 체크하는 것도 알게되었어
# 그렇지만 저 all이란 메서드는 처음보는군
