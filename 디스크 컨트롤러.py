import heapq

def solution(jobs:list):
    q = [] # 큐에는 대기열로 작동한다.
    times = []
    processed_ps = set() # jobs에서 탐색된 녀석들을 저장한다.
    # 동시에 시작하는 녀석들을 우선순위큐에 저장한다.
    prev_start, prev_duration = jobs[0]
    heapq.heappush(q, (prev_duration, prev_start) )
    processed_ps.add((prev_duration, prev_start))
    same_time_ps = [(job[1], job[0]) for job in jobs if ((job[1], job[0]) not in processed_ps) and (job[0] == prev_start)]
    while(same_time_ps):
        p = same_time_ps.pop()
        heapq.heappush(q, p)
        processed_ps.add(p)
    
    #위의 코드가 참 맘에 안든다...
    


    # 0초에 만약 긴 녀셕이 들어오고 1초에 만약 짧은 녀석이 들어온다면...? 1초에 들어온 짧은 녀석을 먼저 처리하는게 낫지 않을까?
    start_time = q[0][1]
    # 여기서부터가 중요하다.
    while(q):
        next_p = heapq.heappop(q) # 구조는 [소요시간, 요청시간]
        processing_time = start_time - next_p[1] + next_p[0]
        start_time = start_time + next_p[0] # 하나의 프로세스가 끝나고 새로운 프로세스의 시작 시간.
        times.append(processing_time)        
        new_processes = [(job[1], job[0]) for job in jobs if ((job[1], job[0]) not in processed_ps) and (job[0] <= start_time)]
        while(new_processes):
            p = new_processes.pop()
            heapq.heappush(q,p)
            processed_ps.add(p)
    return (sum(times)/len(times))

def solution2(jobs:list):
    q = [] # 큐에는 대기열로 작동한다.
    times = []
    # 동시에 시작하는 녀석들을 우선순위큐에 저장한다.
    prev_start, prev_duration = jobs[0]
    heapq.heappush(q, (prev_duration, prev_start) )
    point = 0
    for _ in len(jobs):
        
    
    
    
    
    
    same_time_ps = [(job[1], job[0]) for job in jobs if ((job[1], job[0]) not in processed_ps) and (job[0] == prev_start)]
    while(same_time_ps):
        p = same_time_ps.pop()
        heapq.heappush(q, p)
        processed_ps.add(p)
    # 0초에 만약 긴 녀셕이 들어오고 1초에 만약 짧은 녀석이 들어온다면...? 1초에 들어온 짧은 녀석을 먼저 처리하는게 낫지 않을까?
    start_time = q[0][1]
    # 여기서부터가 중요하다.
    while(q):
        next_p = heapq.heappop(q) # 구조는 [소요시간, 요청시간]
        processing_time = start_time - next_p[1] + next_p[0]
        start_time = start_time + next_p[0] # 하나의 프로세스가 끝나고 새로운 프로세스의 시작 시간.
        times.append(processing_time)        
        new_processes = [(job[1], job[0]) for job in jobs if ((job[1], job[0]) not in processed_ps) and (job[0] <= start_time)]
        while(new_processes):
            p = new_processes.pop()
            heapq.heappush(q,p)
            processed_ps.add(p)
    return (sum(times)/len(times))

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution2([[0, 3], [1, 9], [2, 6]]))

# 우선 처음에 시작하는 녀석들 중에서 똑같은 시간에 시작하는 것을 대기열인 q에 넣어야 할것 아닌가?
# 어떻게? 꼭 0초에 시작하는 것이 아닐 수 있으니 처음과 2번째 그리고 그 이후의 녀석들이 같다는 정보를 얻어야지
# jobs에서 특정조건을 만족하는 녀석들만 소모시키면서 빼내는 것을 어케하지? 한녀석만 빠져나가고 그 이후에는 index가 망가져서 제대로 안된듯.
# 그렇다면 최대한 기존의 jobs을 안건드리는 방향으로? 