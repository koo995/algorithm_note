import math

def solution(picks, minerals):
    sub_minerals = [minerals[i*5:i*5+5] for i in range(math.ceil(len(minerals)/5))]
    for idx, sub_mineral in enumerate(sub_minerals):
        prio = count_prio(sub_mineral)
        sub_minerals[idx].append(prio)
    if sum(picks) >= len(sub_minerals):
        sub_minerals.sort(key=lambda x:x[-1], reverse=True)    
    else: 
        dif = len(sub_minerals)-sum(picks)
        sub_minerals = sub_minerals[:-dif]
        sub_minerals.sort(key=lambda x:x[-1], reverse=True)
    result = 0
    for sub_mineral in sub_minerals: 
        if picks[0] != 0: # 다이아 도끼를 쓰는 경우 항상 5?
            result += count_fatigue(sub_mineral, 0)
            picks[0] -= 1
        elif picks[1] != 0: # 철을 쓰는 경우
            result += count_fatigue(sub_mineral, 1)
            picks[1] -= 1
        elif picks[2] != 0: # 돌을 쓰는 경우
            result += count_fatigue(sub_mineral, 2)
            picks[2] -= 1
        else: break # 모두 다 0 이란 것이니까... 곡괭이를 다 쓴 경우
    return result

def count_fatigue(bunch, p):
    result = 0
    bunch.pop()
    table = [{'diamond': 1, 'iron': 1, 'stone': 1},
            {'diamond': 5, 'iron': 1, 'stone': 1},
            {'diamond': 25, 'iron': 5, 'stone': 1}]
    pick = table[p]
    for b in bunch:
        result += pick[b]
    return result
    
def count_prio(bunch):
    result = 0
    table = {'diamond': 25, 'iron': 5, 'stone': 1}
    for i in bunch:
        result += table[i]
    return result


# 곡괭이가 먼저 소모되는 경우 마지막 녀석은 어짜피 못쓰니까 아니지... 마지막 앞 앞 녀석도 못 캘 수도? 곡괭이가 캘 수 있는데까지 우선순위 고려하면 되겠네
# 여기 이 부분 반드시 알아가자 minerals[a:b]이렇게 할때 b가 전체 길이보다 크더라도 index 에러는 발생하지 않고 마지막까지 가준다.