directions = ["E","W","N","S"]
def solution(park, routes):
    pos = []
    # start 지점을 찾았다.
    for i, row in enumerate(park):
        start_index = row.find("S") # 대소문자 주의
        if start_index != -1: # 이 문법 반드시 기억하지 없으면 -1 반환
            pos = [i, start_index]
    print("시작위치",pos)
    # 명령을 처리하자
    for order in routes :
        direction, dist = order.split() 
        dist = int(dist)
        if direction == "E":
            next_pos = [None, None]
            go_check = False
            for i in range(1,dist+1):
                next_pos = [pos[0], pos[1] + i]
                if next_pos[1] >= 0 and next_pos[1] < len(park[0]) and park[next_pos[0]][next_pos[1]] == "O":
                        go_check = True
                else: 
                    go_check = False
                    break
            if go_check == True: # 언제 go_check을 True로 해줄것이냐? 
                # 모든 이동에 대해서 ok일때 인데... 모든 이동에 대해서 ok는 어떻게 처리할까?
                pos = next_pos
                print("현재위치: ", pos)
        if direction == "W":
            next_pos = [None, None]
            go_check = False
            for i in range(1,dist+1):
                next_pos = [pos[0], pos[1] - i]
                if next_pos[1] >= 0 and next_pos[1] < len(park[0]) and park[next_pos[0]][next_pos[1]] == "O":
                        go_check = True
                else: 
                    go_check = False
                    break
            if go_check == True: # 언제 go_check을 True로 해줄것이냐? 
                # 모든 이동에 대해서 ok일때 인데... 모든 이동에 대해서 ok는 어떻게 처리할까?
                pos = next_pos
                print("현재위치: ", pos)

        if direction == "S":
            next_pos = [None, None]
            go_check = False
            for i in range(1,dist+1):
                next_pos = [pos[0] + i, pos[1]]
                if next_pos[0] >= 0 and next_pos[0] < len(park) and park[next_pos[0]][next_pos[1]] == "O":
                        go_check = True
                else: 
                    go_check = False
                    break
            if go_check == True: # 언제 go_check을 True로 해줄것이냐? 
                # 모든 이동에 대해서 ok일때 인데... 모든 이동에 대해서 ok는 어떻게 처리할까?
                pos = next_pos
                print("현재위치: ", pos)

        if direction == "N":
            next_pos = [None, None]
            go_check = False
            for i in range(1,dist+1):
                next_pos = [pos[0] - i , pos[1]]
                if next_pos[0] >= 0 and next_pos[0] < len(park) and park[next_pos[0]][next_pos[1]] == "O":
                        go_check = True
                else:
                    go_check = False
                    break
            if go_check == True: # 언제 go_check을 True로 해줄것이냐? 
                # 모든 이동에 대해서 ok일때 인데... 모든 이동에 대해서 ok는 어떻게 처리할까?
                pos = next_pos
                print("현재위치: ", pos)

    answer = pos
    return answer


            
    
    
# 시간 복잡도를 고려하지 않기가 어렵네
# start 지점을 어떻게 특정하지?
# 어디서 IndexError: string index out of rang 이게 뜨는거지
# park의 최대 크기를 고려안했네
# 더불어서 pos가 새롭게 초기화 되었네...
# 가는길에 x가 있으면 안되는 것이군...
# map함수를 썻는데 그건 함수와 iteratal을 받지...
# 왤케 짜잘한 실수를 많이 했지? and or도 헷갈리고...
# 특정한 조건의 변수를 따로 둬서 조건이 만족되면 움직인다는게 좋구나
# false가 되었을 때 반복문을 나온는것도 체크해야지...