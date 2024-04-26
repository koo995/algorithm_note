def solution():
    def board_to_array():
        point = shark_point
        cycle_pattern = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cycle = 1
        array = []
        zero_flag = False
        while not zero_flag:
            for i in range(4):
                if zero_flag:
                    break
                for _ in range(2 * cycle - (1 if i < 2 else 0)):
                    if zero_flag:
                        break
                    y, x = point
                    dy, dx = cycle_pattern[i]
                    point = (y + dy, x + dx)
                    array.append((point, bead_board[point[0]][point[1]]))
                    if point == (0, 0) or bead_board[point[0]][point[1]] == 0:
                        zero_flag = True
            cycle += 1
        return array

    def get_effected_points(d, s):
        direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
        dy, dx = direction[d]
        point = shark_point
        effected_points = []
        for i in range(1, s + 1):
            effected_points.append((point[0] + dy * i, point[1] + dx * i))
        return effected_points

    def remove_continuous_beads(*arrays):
        no_continuous = False
        arrays = list(*arrays)
        arrays.append(0)
        while not no_continuous:
            stack = []
            no_continuous = True
            for idx, bead in enumerate(arrays):
                if stack and arrays[stack[-1]] != bead:
                    if len(stack) >= 4:
                        no_continuous = False
                        prev_bead = arrays[stack[-1]]
                        bead_count[prev_bead] += len(stack)
                        while stack:
                            top_idx = stack.pop()
                            arrays[top_idx] = 0
                    else:
                        stack.clear()
                stack.append(idx)
            # 모든 반복되는 녀석들은 다 0으로 처리했으니까... 모두 삭제하자 그것보단... 0인 것을 제외하고 새롭게 만들어나갈까?
            new_array = []
            for element in arrays:
                if element == 0:
                    continue
                new_array.append(element)
            arrays = new_array
        return arrays

    def update_bead_group(arrays):
        # 좌표값은 필요없으니까 없앤다.
        stack = []
        arrays.append(0)
        updated_bead_array = []
        for num in arrays:
            if stack and stack[-1] != num:  # 여기에서 여전히... stack이 남은 경우를 고려 안했구나... tmp에 임의로 0하나 추가함.
                size = len(stack)
                bead_num = stack[-1]
                updated_bead_array.append(size)
                updated_bead_array.append(bead_num)
                stack.clear()
            stack.append(num)
        return updated_bead_array

    def array_to_board(arrays):
        # 자... 현재 가지고 있는 배열을 다시 board에 업데이트 해줘야 한다.
        point = shark_point
        cycle_pattern = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cycle = 1
        board = [[0] * N for _ in range(N)]
        arr_idx = 0
        arr_size = len(arrays)
        stop = False
        while not stop:
            for i in range(4):
                if stop:
                    break
                for _ in range(2 * cycle - (1 if i < 2 else 0)):
                    y, x = point
                    dy, dx = cycle_pattern[i]
                    if not (0 <= y + dy < N and 0 <= x + dx < N) or arr_idx == arr_size:
                        stop = True
                        break
                    board[y + dy][x + dx] = arrays[arr_idx]
                    arr_idx += 1
                    point = (y + dy, x + dx)  # 변경된 포인트 업데이트 안해서 한참 해맸다...
            cycle += 1
        return board

    N, M = map(int, input().split())
    bead_board = [list(map(int, input().split())) for _ in range(N)]
    magic_infos = [list(map(int, input().split())) for _ in range(M)]
    bead_count = {1: 0, 2: 0, 3: 0}
    shark_point = (-1 + (N + 1) // 2, -1 + (N + 1) // 2)
    for di, si in magic_infos:
        bead_arrays = board_to_array()
        effected_points = get_effected_points(di, si)
        for point, bead in bead_arrays[::-1]:
            if point in effected_points:
                bead_arrays.remove((point, bead))
        removed_arrays = remove_continuous_beads(bead for _, bead in bead_arrays)
        updated_bead_arrays = update_bead_group(removed_arrays.copy())
        bead_board = array_to_board(updated_bead_arrays)
    print(1 * bead_count[1] + 2 * bead_count[2] + 3 * bead_count[3])


solution()
