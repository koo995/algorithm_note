#게임 개발
n,m = map(int, input().split())
a,b,d = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

class Player:
    moves = [[0,-1],[1,0],[0,1],[-1,0]]
    directions = [0, 1, 2, 3]
    
    def __init__(self, x = a, y = b, d = d):
        self.x = x
        self.y = y
        self.d = d
        self.visited = [[0]*(m) for _ in range(n)]
        self.visited[y][x] = 1
        self.cnt_visit = 1
        self.rot_time = 0
    
    def rotate(self):
        self.d -=1 
        if self.d < 0:
            self.d = 3
    
    def get_loc(self):
        return self.x, self.y
    
    def get_direction(self):
        return self.d
    
    def set_visit(self, x, y):
        self.visited[y][x] = 1
    
    def check_visit(self, x, y):
        return self.visited[y][x] == 1
    
    def check_sea(self, x, y):
        return array[y][x] == 1
    
    def get_next_loc(self):
        move = Player.moves[Player.directions.index(self.d)]
        next_x = self.x + move[0]
        next_y = self.y + move[1]
        return next_x, next_y
        
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
        self.cnt_visit += 1
        self.set_visit(self.x, self.y)
             
    def check_boundary(self, nx, ny):
        return nx >=0 and nx < m and ny >=0 and ny < n
    
    def back_move(self):
        self.rotate()
        self.rotate()
        nx, ny = self.get_next_loc()
        self.x = nx
        self.y = ny
        self.rotate()
        self.rotate()
        if self.check_sea(self.x, self.y) \
            or not self.check_boundary(self.x, self.y):
            return -1
        else:
            return 1
                    
player1 = Player(a,b,d)
while True:
    player1.rotate()
    nx, ny = player1.get_next_loc()
    if player1.check_sea(nx,ny) \
        or player1.check_visit(nx, ny) \
            or not player1.check_boundary(nx,ny):
        player1.rot_time += 1
        if player1.rot_time == 4:
            result = player1.back_move()
            player1.rot_time = 0
            if result == -1:
                break
        continue
    player1.move(nx, ny)
    player1.rot_time = 0
    
print(player1.cnt_visit)
        
# 참고 좌표를 고려할때 우리는 항상 (0,0)부터 시작하잖아... (1,1)이 첫번째 좌표는 아니지...
#그리고 주피터 노트북은 사용할때 항상 유의하자.... 위에서 쓸모없이 선언한게 잘못 쓰일 수 있으니까...
# 연속적으로 4번 이동불가가 실행되었을 때 그 부분을 체크할 방법이 따로 없을까? 정상 작동에서 rot_time = 0으로 초기화 하지 않고...
