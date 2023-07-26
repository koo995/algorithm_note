direct = ["E", "W", "S", "N"]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(park, routes):
    pos = [[h, p.index("S")] for h, p in enumerate(park) if "S" in p][0]
    for route in routes:
        # "E 2" 이런 형식을 가짐.
        op, n = route.split(" ")
        n_pos = []
        permission = False
        for n_d in range(1,int(n)+1):
            n_pos = move(pos, op, n_d)
            if 0 <= n_pos[0] < len(park) \
                and 0 <= n_pos[1] < len(park[0]) \
                and park[n_pos[0]][n_pos[1]] !="X":
                permission = True
            else:
                permission = False
                break # 안되는게 있다면 더이상 안간다.
        if permission == True:
            pos = n_pos
    return pos
            
def move(pos, op, n):
    op_idx = direct.index(op)
    n_x = pos[1] + dx[op_idx] * n
    n_y = pos[0] + dy[op_idx] * n
    return [n_y, n_x]



print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))