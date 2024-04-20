def solution():
    from collections import defaultdict
    
    N = int(input())
    infos = [map(int, input().split()) for _ in range(N*N)]
    scores = {0:1, 1:1, 2:10, 3:100, 4:1000}
    table = [[0] * N for _ in range(N)]
    student_point = defaultdict(tuple)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def find_seat1(a, b, c, d) -> list[tuple[int]]:
        tmp = [[0] * N for _ in range(N)]
        max_value = -1
        for y in range(N):
            for x in range(N):
                # 누군가가 앉아 있다면 제외한다.
                if table[y][x] != 0:
                    continue
                # 특정 자리에서 주변을 살핀다.
                for idx in range(4):
                    if not (0 <= y + dy[idx] < N and 0 <= x + dx[idx] < N):
                        continue
                    if table[y + dy[idx]][x + dx[idx]] in [a, b, c, d]:
                        tmp[y][x] += 1
                        max_value = max(max_value, tmp[y][x])
        # 이제 맥스 값에 해당하는 자리들을 찾는다.
        # 하지만 하나도 해당되는 녀석이 없어서 -1 그대로라면?
        answer = []
        for y in range(N):
            for x in range(N):
                if max_value == -1:
                    if table[y][x] == 0:
                        answer.append((y, x))
                    continue
                if tmp[y][x] == max_value:
                    answer.append((y, x))
        return answer
        
    def find_seat2(ss) -> list[tuple[int]]:
        answer = []
        max_value = -1
        # ss에 있는 후보들 중에서 인접한 칸 중에서 비어있는 칸이 가장 많은 칸을 넘긴다.
        for s in ss:
            # 위치 s에 대해서 인접한 칸에 비어있는 칸이 몇개인지 확인해보자
            y, x = s
            count = 0
            for idx in range(4):
                if not (0 <= y + dy[idx] < N and 0 <= x + dx[idx] < N):
                    continue
                if table[y + dy[idx]][x + dx[idx]] == 0:
                    count += 1
            if count > max_value:
                max_value = count
                answer.clear()
            if count == max_value:
                answer.append(s)
        return answer
    
    def find_seat3(ss) -> tuple[int]:
        ss.sort(key = lambda s:(s[0], s[1]))
        return ss
    
    friend_dic = {}
    for idx, info in enumerate(infos.copy()):
        stu, f1, f2, f3, f4 = info
        friend_dic[stu] = [f1, f2, f3, f4]
        if idx == 0:
            table[1][1] = stu
            student_point[stu] = (1,1)
            continue
        seats = find_seat1(f1, f2, f3, f4)
        if len(seats) > 1:
            seats = find_seat2(seats.copy())
        if len(seats) > 1:
            seats = find_seat3(seats.copy())
        s = seats.pop(0)
        table[s[0]][s[1]] = stu
        student_point[stu] = s
    total_score = 0    
    
    for y in range(N):
        for x in range(N):
            count = 0
            for idx in range(4):
                if not (0 <= y + dy[idx] < N and 0 <= x + dx[idx] < N):
                    continue
                if table[y + dy[idx]][x + dx[idx]] in friend_dic[table[y][x]]:
                    count += 1
            total_score += scores[count]
    print(total_score)
    
def solution2():
    n = int(input())
    data = [[0] * n for _ in range(n)]
    students = [list(map(int, input().split())) for _ in range(n**2)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for student in students:
        available = []

        for i in range(n):
            for j in range(n):
                # 빈자리가 있다면
                if data[i][j] == 0:
                    prefer, empty = 0, 0
                    
                    # 동서남북 방향 확인하여 
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        # 범위내에 있을 때
                        if 0 <= nx < n and 0 <= ny < n:
                            # 좋아하는 학생이 주위에 있다면 더해준다.
                            if data[nx][ny] in student[1:]:
                                prefer += 1
                                
                            # 빈자리가 있다면 더해준다.
                            if data[nx][ny] == 0:
                                empty += 1

                    available.append((i, j, prefer, empty))
        # 정렬
        available.sort(key= lambda x: (-x[2], -x[3], x[0], x[1]))
        data[available[0][0]][available[0][1]] = student[0]

    answer = 0
    score = [0, 1, 10, 100, 1000]
    students.sort()

    for i in range(n):
        for j in range(n):
            count = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if data[nx][ny] in students[data[i][j] - 1]:
                        count += 1

            answer += score[count]

    print(answer)

    solution()