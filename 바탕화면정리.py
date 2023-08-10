def solution(wallpaper):
    INF = int(1e9)
    minY = INF
    minX = INF
    maxY = -INF
    maxX = -INF
    for y, row in enumerate(wallpaper):
        if "#" in row:
            min_x = row.find("#")
            max_x = row.rfind("#")
            minY = min(y, minY)
            minX = min(min_x, minX)
            maxY = max(y, maxY)
            maxX = max(max_x, maxX)
    answer = [minY, minX, maxY+1, maxX+1]
    return answer
 # 아하 하나의 row에서 제일 끝에 있는 경우도 있을 수 있군...


# max에서는 x, y 에 1을 추가해줘야 포함될듯
# 어짜피 드래그는 좌상에서 우하방향
# enumerate을 enumerator이라 했네..
# x와 y의 좌표가 y,x
# max_x의 값이 틀렸는데 find함수는 찾을려는 것의 제일 첫번째 index을 반환하지... 역순으로 못하나
# 그리고 #을 쓸때 \ 이거 필요없네... 문자열 안에는