from collections import deque

N = int(input()) # 보드의 크기 100*100
K = int(input()) # 사과의 갯수 100개 까지 
apples = [list(map(int,input().split())) for _ in range(K)] # 사과의 좌표
L = int(input()) # 뱀의 방향 전환 횟수
moves = [(lambda x: [int(x[0]), x[1]])(input().split()) for _ in range(L)] # 뱀의 방향전환
# [[3, 'D'], [15, 'L'], [17, 'D']]

map = [[]]
# 다이렉션을 어떻게 처리할까?
rotate = ["L", "D"]
directions = [[-1, 0],[0, 1],[1, 0],[0, -1]] # 북동남서
cur_direction = 1 # 오른쪽이 시작이니까?

snake = deque()
snake.append([1,1])

for t in range(1, 1e4):
    # 머리를 다음 칸에 위치 시킨다.
    head = snake[-1]
    pre_head = [head[0] + directions[cur_direction][0], head[1] + directions[cur_direction][1]]
    snake.append(pre_head)
    # 벽에 부딪힌 경우, 몸에 부딪힌 경우
    if not(1 <= pre_head[0] <= N and 1 <= pre_head[1] <= N) \
            or pre_head in list(snake)[:-1]:
        print(t) # 몇초인지 출력하고 끝
        break
    # 이동한 칸에 사과가 있다면
    if pre_head in apples:
        apples.remove(pre_head)
    # 사과가 없다면
    else :
        snake.popleft()
    # 초가 끝난 다음에 방향전환
    for i in range(L):
        if moves[i][0] == t:
            if moves[i][1] == "L":
                cur_direction = (cur_direction + 3) % 4
            else: # "D" 인 경우
                cur_direction = (cur_direction + 5) % 4
        
# 람다식 조작하는거 유의하고
# 리스트 선회하는거 유의하지
# 자신의 몸에 닿았다 라는 것을 어케 할까