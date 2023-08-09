def solution(board):
    directions = ["n", "w", "e", "s"]
    # 먼저 위치를 찾는게 맞는거 같아.
    r_pos = []
    g_pos = []
    for idx, row in enumerate(board):
        if "R" in row:
            r_x_i = row.find("R")
            r_pos = [idx, r_x_i]
        if "G" in row:
            g_x_i = row.find("G")
            g_pos = [idx, g_x_i]
    print("현재위치: ",r_pos)
    print("목표: ", g_pos)
    results = [] # 여기는 G을 찾았을 때의 모든 cnt값을 담아주는 거야.
    cnt = 0
    def recur_fn(pos, cnt): # 그래서 이 함수는 무엇을 반환해야 할까? G을 찾았을때의 cnt값
        for d in range(4):
            next_pos = slide_to_end(pos,d, board)
            print("nextpos: ", next_pos)
            # if next_pos != pos:
            #     cnt += 1
            # # 끝낼 조건을 명시해야 할텐데... 못찾는다는건 어케하지?
            # if next_pos == g_pos and
            #     return cnt
    recur_fn(r_pos,cnt)
            
                
            
    answer = 0
    return answer

def slide_to_end(pos, d, board):
    # d는 0 1 2 3
    next_pos = [pos[0], pos[1]]
    if d == 0: # 동
        for n in range(len(board[0])):
            pos_x = pos[1] + n
            if check_end([pos[0], pos_x], board):
                next_pos = [pos[0], pos_x-1]
                return next_pos
    elif d == 1: # 서
        for n in range(len(board[0])):
            pos_x = pos[1] - n
            if check_end([pos[0], pos_x], board):
                next_pos = [pos[0], pos_x+1]
                return next_pos
    elif d == 2: # 남
        for n in range(len(board)):
            pos_y = pos[0] + n
            if check_end([pos_y, pos[1]], board):
                next_pos = [pos_y-1, pos[1]]
                return next_pos
    else: # 북
        for n in range(len(board)):
            pos_y = pos[0] - n
            if check_end([pos_y, pos[1]], board):
                next_pos = [pos_y+1, pos[1]]
                return next_pos

def check_end(pos, board):
    if pos[0] >= len(board) or pos[0] < 0 or\
        pos[1] < 0 or pos[1] >= len(board[0]) or\
        board[pos[0]][pos[1]] == "D":
        return True
    
    