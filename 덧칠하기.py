def solution(n, m, section):
    count = 0
    walls_table = [1] * (n+1)
    # 칠해진 영역은 section에서 제거해 버리는거야.
    # 어떻게 제거하지? 칠한 영역을 따로 저장해야할듯
    
    # 파손된 wall 은 0으로만듬
    for f_wall in section: # 최대 10만인가
        walls_table[f_wall] = 0
    
    # 이제부터 페인트칠을 하자
    for f in section:
        if walls_table[f] == 1:
            continue
        for dm in range(m):
            if f+dm <= n:
                walls_table[f+dm] = 1
        count +=1
        
        
    answer = count
    return answer


# NameError: name 'coutinue' is not defined 에러가 뜨는 데 왜지?