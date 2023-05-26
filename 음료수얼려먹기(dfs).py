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

def dfs(i, j):
    visited[i][j] = 1
    print("여기 방문했어: ", (i,j))
    for move in moves:
        print("무브", move)
        if not check_boundary(i + move[0],j + move[1]):
            print("boundary")
            continue
        if array[i + move[0]][j + move[1]] == 0 \
            and not visited[i + move[0]][j + move[1]]:
            dfs(i + move[0], j + move[1])
    


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and not array[i][j] == 1:
            print("여기서 bfs 수행: ", [i,j], count)
            dfs(i, j)
            count += 1

print(count)    