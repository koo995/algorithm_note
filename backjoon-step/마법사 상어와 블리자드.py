def solution():
    def get_flat_array(point):
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
                    array.append((point, bead_table[point[0]][point[1]]))
                    if point == (0, 0) or bead_table[point[0]][point[1]] == 0:
                        zero_flag = True
            cycle += 1
        return array

    def get_effected_points(d, s):
        direction = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
        dy, dx = direction[d]
        point = shark_point
        results = []
        for i in range(1, s + 1):
            results.append((point[0] + dy * i, point[1] + dx * i))
        return results
    
    def remove_continuous_beads(arrays:list):
        no_continuous = False
        temp_arrays = arrays.copy()
        while not no_continuous: 
            stack = []
            no_continuous = True
            for idx, element in enumerate(temp_arrays): 
                if (stack and temp_arrays[stack[-1]][1] != element[1]):
                    if len(stack) >= 4:
                        no_continuous = False
                        point, bead = temp_arrays[stack[-1]]
                        bead_count[bead] += len(stack)
                        while stack:
                            top_idx = stack.pop()
                            temp_arrays[top_idx] = 0
                    else:
                        stack.clear()
                stack.append(idx)
            # 모든것을 다 탐색했는데... 남은 stack 역시 4 이상이라면...
            if stack and len(stack) >= 4:
                no_continuous = False
                point, bead = temp_arrays[stack[-1]]
                bead_count[bead] += len(stack)
                while stack:
                    top_idx = stack.pop()
                    temp_arrays[top_idx] = 0
            # 모든 반복되는 녀석들은 다 0으로 처리했으니까... 모두 삭제하자 그것보단... 0인 것을 제외하고 새롭게 만들어나갈까?
            new_array = []
            for element in temp_arrays:
                if element == 0:
                    continue
                new_array.append(element)
            temp_arrays = new_array
        return temp_arrays

    def update_bead_group(arrays):
        # 좌표값은 필요없으니까 없앤다.
        tmp = []
        result = []
        for point, bead in arrays:
            tmp.append(bead)
        tmp.append(0)
        # 여전히 stack을 써서 역순으로 가야할까?
        stack = []
        for num in tmp:
            if stack and stack[-1] != num: # 여기에서 여전히... stack이 남은 경우를 고려 안했구나...
                size = len(stack)
                bead_num = stack[-1]
                result.append(size)
                result.append(bead_num)
                stack.clear()
            stack.append(num)
        return result
    
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
                if stop == True:
                    break
                for _ in range(2 * cycle - (1 if i < 2 else 0)):
                    y, x = point
                    dy, dx = cycle_pattern[i]
                    if not (0 <= y+dy < N and 0 <= x+dx < N) or arr_idx == arr_size:
                        stop = True
                        break
                    board[y + dy][x + dx] = arrays[arr_idx]
                    arr_idx += 1
                    point = (y + dy, x + dx)
            cycle += 1
        return board
    
    
    N, M = map(int, input().split())
    bead_table = [list(map(int, input().split())) for _ in range(N)]
    magic_infos = [list(map(int, input().split())) for _ in range(M)]
    bead_count = {1:0, 2:0, 3:0}
    shark_point = (-1 + (N+1) // 2, -1 + (N+1) // 2)
    for di, si in magic_infos:
        table_array = get_flat_array(shark_point)
        effected_points = get_effected_points(di, si)
        for point, bead in table_array[::-1]: 
            if point in effected_points:
                table_array.remove((point, bead))
        removed_arrays = remove_continuous_beads(table_array)
        updated_bead_array = update_bead_group(removed_arrays)
        bead_table = array_to_board(updated_bead_array)
    print(1 * bead_count[1] + 2 * bead_count[2] + 3 * bead_count[3])

solution()