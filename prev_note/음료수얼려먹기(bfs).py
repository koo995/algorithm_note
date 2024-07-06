#음료수 얼려먹기
from collections import deque


n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input())))
print(array)

visited = [[0]*(m) for _ in range(n)]
count = 0
moves = [[0,-1], [1,0], [0,1], [-1,0]] #좌 하 우 상

def check_boundary(i,j):
    return i >=0 and i < n and j >=0 and j < m

def bfs(i, j):
    global visited
    global array
    q = deque() #큐에 들어갈 값이 뭔지 정확히 인식하자
    node = (i,j)
    q.append(node)
    
    while q:
        i,j = q.popleft()
        print("현재 노드: ", (i, j))
        visited[i][j] = 1
        # print(currnet_node)
        for move in moves:
            nextI = i + move[0]
            nextJ = j + move[1]
            if not check_boundary(nextI, nextJ):
                continue
            if array[nextI][nextJ] == 0 \
                and not visited[nextI][nextJ]:
                n_node = (i+move[0], j+move[1])
                visited[nextI][nextJ] = 1
                q.append(n_node)
    
    return True


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and not array[i][j] == 1:
            print("여기서 bfs 수행: ", [i,j], count)
            bfs(i, j)
            count += 1
        

#뭔가 찜찜하다... 중복되는 녀석들이 queue에 들어가잔항...
#그리고 굳이 visited 테이블은 만들 필요가 없었나...
#튜플로 언팩킹해서 i,j 로 하는게 node[0][1]이런식보다는 훨씬 깔끌한거 같다...



print(count)    