import math

def solution(r1, r2):
    result = r2 -r1 +1 # x좌표가 0일 때 
    for x in range(1, r2): # 마지막 r2인 지점은 y값이 0이 된다.
        max_y = math.floor(math.sqrt(math.pow(r2, 2) - math.pow(x, 2)))
        min_y = math.floor(math.sqrt(math.pow(r1, 2) - math.pow(x, 2))) if r1 > x else 0
        result += (max_y - min_y)    
    return result * 4

print(solution(1,3))
# 런타임 에러가 왜 뜨는 거지? math.sqrt 안에는 음수가 오면 안되는 것이지...
# 어디서 계속 실패가 뜨는 것일까?