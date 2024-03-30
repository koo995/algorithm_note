def solution():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]  # 문자열을 굳이 리스트로 바꿀 필요는 없겠다.

    def count_chess(i_start: int, j_start: int) -> int:
        # y, x 을 시작점으로 8 만큼 이동한 녀석들에게서 얼마만큼 갯수를 체워야 하는지 계산한다.
        # 여기서 빠르게 체크하는 방법은 어떤게 있을까? 하나하나 다 체크한다고 하더라도... 마냥 쉽지많은 않네
        correct_chess = [
            ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"],
            ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]]
        count_1 = 0
        count_2 = 0
        for i_idx, i in enumerate(range(i_start, i_start + 8)):
            for j_idx, j in enumerate(range(j_start, j_start + 8)):
                if board[i][j] != correct_chess[0][i_idx][j_idx]:
                    count_1 += 1
                elif board[i][j] != correct_chess[1][i_idx][j_idx]:
                    count_2 += 1
        return min(count_1, count_2)

    min_count = int(1e9)
    for i in range(0, N - 7):
        for j in range(0, M - 7):
            min_count = min(min_count, count_chess(i, j))
    print(min_count)


solution()
