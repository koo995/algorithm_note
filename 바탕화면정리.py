def solution(wallpaper):
    min_x = int(1e9)
    min_y = int(1e9)
    max_x = -int(1e9)
    max_y = -int(1e9)
    
    for w_y, row in enumerate(wallpaper):
        # 전체 모양 출력
        print(w_y, row)
        
        # row에서 #을 찾는다. 그리고 최대 최소 갱신
        index = row.find("#")
        if index != -1: # 샵을 찾는다 없으면 -1, 찾으면 index 반환
            laxt_index = row.rfind("#")
            w_x = index
            w_x_r = laxt_index
            min_x = min(min_x, w_x)
            min_y = min(min_y, w_y)
            max_x = max(max_x, w_x_r + 1)
            max_y = max(max_y, w_y + 1)
            
    answer = [min_y, min_x, max_y, max_x]
    return answer


# max에서는 x, y 에 1을 추가해줘야 포함될듯
# 어짜피 드래그는 좌상에서 우하방향
# enumerate을 enumerator이라 했네..
# x와 y의 좌표가 y,x
# max_x의 값이 틀렸는데 find함수는 찾을려는 것의 제일 첫번째 index을 반환하지... 역순으로 못하나
# 그리고 #을 쓸때 \ 이거 필요없네... 문자열 안에는