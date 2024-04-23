def solution():
    def find_seat(*prefer_friends):
        table_cond_info = []
        for y in range(N):
            for x in range(N):
                # 현 위치가 비어있지않다면 제외
                if table[y][x] != 0:
                    continue
                # 각 칸마다 인접한 칸들을 확인한다. 현 위치에서 인접한 칸에 비어있는 녀석은 몇개인지, 좋아하는 녀석은 몇명인지 판단한다.
                prefer_count, empty_count = 0, 0
                for i in range(4):
                    # 테이블범위를 넘어가면 제외
                    n_y = y + dy[i]
                    n_x = x + dx[i]
                    if not (0 <= n_y < N and 0 <= n_x < N):
                        continue
                    # 인접한 칸이 비어있다면 카운팅해준다.
                    if table[n_y][n_x] == 0:
                        empty_count += 1
                        continue
                    # 인접한 칸에 좋아하는 사람이 있다면 카운팅해준다.
                    if table[n_y][n_x] in prefer_friends:
                        prefer_count += 1
                table_cond_info.append((prefer_count, empty_count, y, x)) # 좋아하는 사람이 몇명인지, 빈자리는 몇명인지 현위치 정보 저장
        table_cond_info.sort(key=lambda info:(-info[0], -info[1], info[2], info[3]))
        # 정렬을 했는데... 여기서 어떻게 한 자리를 정하지? 기본적으로 400개가 정렬이 되었을 것이다. 그렇지.. 제일 첫 녀석이 이것을 만족하는 녀석이겠지
        return (table_cond_info[0][2], table_cond_info[0][3])
    
    N = int(input())
    prefer_infos = [list(map(int, input().split())) for _ in range(N**2)]
    prefer_infos_dic = {}
    table = [[0] * N for _ in range(N)] # N * N 테이블의 자리배치를 기록한다.
    score_dic = {0:0, 1:1, 2:10, 3:100, 4:1000}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 먼저 학생 한명한명 자리를 정해나가야겠다.
    for s, f1, f2, f3, f4 in prefer_infos: # 최대 400 이다.
        prefer_infos_dic[s] = (f1, f2, f3, f4)
        # 여기서 table을 모두 탐색할까? 그리고 4방향도 모두 탐색? 그러면 최대 1600이다. 400 * 1600 = 640000 이면 할만한데?
        y, x = find_seat(f1, f2, f3, f4)
        table[y][x] = s
    total_score = 0
    for y in range(N):
        for x in range(N):
            s = table[y][x]
            count = 0
            # 인접한 테이블을 확인한다.
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if not (0 <= n_y < N and 0 <= n_x < N):
                    continue
                if table[n_y][n_x] in prefer_infos_dic[s]:
                    count += 1
            total_score += score_dic[count]
    print(total_score)
    
    
solution()