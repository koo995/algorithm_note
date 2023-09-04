N = int(input()) # 보드의 크기
K = int(input()) # 사과의 갯수
apples = [list(map(int,input().split())) for _ in range(K)] # 사과의 좌표
L = int(input()) # 뱀의 방향 전환 횟수
moves = [(lambda x: [int(x[0]), x[1]])(input().split()) for _ in range(L)] # 뱀의 이동
