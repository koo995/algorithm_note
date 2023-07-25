from collections import deque


def solution2(plans):
    result = [] # 먼저 끝나는 순서대로 넣는다.
    stack = deque()
    mem = deque()
    plans = [[plan[0], (lambda x: int(x[:2])*60 + int(x[3:]))(plan[1]), int(plan[2])] \
             for plan in plans] # comprehension을 이용한 방법
    plans.sort(key=lambda x:x[1])
    print(plans)
    # [['music', 740, 40], ['computer', 750, 100], ['science', 760, 50], ['history', 840, 30]]
    exit_time = plans[0][1] + plans[0][2]
    mem.append([plan[0][0], exit_time]) # 어쨋든 첫번째 녀석을 일단 넣어준다.
    for plan in plans[1:]: # 두번째 녀석부터 스케쥴링 시작이다.
        new_start_time = plan[1]
        new_exe_time = plan[2]
        cur_plan = mem.pop() # pop은 시간복잡도가 겨우 1이다.
        cur_exit_time = cur_plan[1]
        if new_start_time < cur_exit_time:
            mem.append([plan[0], new_start_time + new_exe_time])
            remain_time = exit_time - new_start_time
            stack.append([cur_plan, remain_time])
        elif new_start_time >= cur_exit_time:
            result.append(cur_plan) # 현재 메모리에 있던 것은 끝났으니 결과에 넣어준다.
            pre_plan = stack.pop()
            pre_remain_t = pre_plan[1]
            mem.append([pre_plan, ])
    return 0

from collections import deque

def solution(plans):
    # lambda 에 인자를 넣는 방법 알아가자
    plans = [[plan[0], (lambda x: int(x[:2])*60 + int(x[3:]))(plan[1]), int(plan[2])] \
             for plan in plans] # comprehension을 이용한 방법
    plans.sort(key=lambda x:x[1])
    results = []
    results.append([plans[0][0], plans[0][1] + plans[0][2]]) # [이름, 끝날 시간]
    for plan in plans[1:]:
        new_plan = plan[0]
        start_time = plan[1]
        exe_time = plan[2]
        results = list(map(lambda x: [x[0], x[1]+exe_time if x[1] > start_time else x[1]], results))
        results.append([new_plan, start_time + exe_time])
    print(results)
    results.sort(key = lambda x: x[1]) # 오름차순이 빨리 끝나는 순서가 될 것이다.
    results = [result[0] for result in results]
    return results
        

# comprehension을 이용한 방법
# plans = [[plan[0], (lambda x: int(x[:2])*60 + int(x[3:]))(plan[1]), int(plan[2])] for plan in plans]
# -2.5510787963867188e-05 시간 소요

# map을 이용한 방법
# plans = list(map(lambda x: [x[0], int(x[1][:2])*60 + int(x[1][3:]), int(x[2])], plans))
# 참고로 map객체에 대해서도 sorted 함수 사용 가능하다
# -2.0265579223632812e-05
# -2.5272369384765625e-05
# -1.9788742065429688e-05

# 속도는 둘다 비슷한가...