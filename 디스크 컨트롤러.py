import heapq


def solution(jobs: list):
    q = []  # 큐에는 대기열로 작동한다.
    times = []
    processed_ps = set()  # jobs에서 탐색된 녀석들을 저장한다.
    # 동시에 시작하는 녀석들을 우선순위큐에 저장한다.
    prev_start, prev_duration = jobs[0]
    heapq.heappush(q, (prev_duration, prev_start))
    processed_ps.add((prev_duration, prev_start))
    same_time_ps = [
        (job[1], job[0])
        for job in jobs
        if ((job[1], job[0]) not in processed_ps) and (job[0] == prev_start)
    ]
    while same_time_ps:
        p = same_time_ps.pop()
        heapq.heappush(q, p)
        processed_ps.add(p)

    # 위의 코드가 참 맘에 안든다...
    # 0초에 만약 긴 녀셕이 들어오고 1초에 만약 짧은 녀석이 들어온다면...? 1초에 들어온 짧은 녀석을 먼저 처리하는게 낫지 않을까?
    start_time = q[0][1]
    # 여기서부터가 중요하다.
    while q:
        next_p = heapq.heappop(q)  # 구조는 [소요시간, 요청시간]
        processing_time = start_time - next_p[1] + next_p[0]
        start_time = start_time + next_p[0]  # 하나의 프로세스가 끝나고 새로운 프로세스의 시작 시간.
        times.append(processing_time)
        new_processes = [
            (job[1], job[0])
            for job in jobs
            if ((job[1], job[0]) not in processed_ps) and (job[0] <= start_time)
        ]
        while new_processes:
            p = new_processes.pop()
            heapq.heappush(q, p)
            processed_ps.add(p)
    return sum(times) / len(times)


def solution2(jobs):
    q = []  # 큐에는 대기열로 작동한다.
    times = []
    jobs_finish = False
    cur_time = 0
    jobs.sort(key=lambda x: x[0])  # 이게 필요할지 몰랐네...
    request_time, duration = jobs[0]
    cur_time = request_time
    heapq.heappush(q, (duration, request_time))
    n_point = 1  # 앞으로 처리해야할 jobs의 포인터
    while n_point < len(jobs) or q:
        for _ in range(len(jobs) - n_point):  # 남은 녀석들의 갯수만큼
            next_p = jobs[n_point]
            next_request_time, next_duration = next_p
            if next_request_time <= cur_time:
                heapq.heappush(q, (next_duration, next_request_time))
                n_point += 1
                if n_point == len(jobs):
                    jobs_finish = True
            elif not q and jobs_finish == False:
                cur_time = next_request_time
                heapq.heappush(q, (next_duration, next_request_time))
                n_point += 1
                if n_point == len(jobs):
                    jobs_finish = True
        now_processing_p = heapq.heappop(q)
        duration, request_time = now_processing_p
        total_processing_time = cur_time - request_time + duration
        cur_time += duration
        times.append(total_processing_time)
    return int(sum(times) / len(times))


def solution3(jobs):
    q = []
    times = []
    cur_time = 0
    jobs.sort(key=lambda x: x[0])
    n_point = 0
    while n_point < len(jobs) or q:
        if q:
            duration, request_time = heapq.heappop(q)
            total_processing_time = cur_time - request_time + duration
            times.append(total_processing_time)
            cur_time += duration
        else:
            cur_time = jobs[n_point][0]

        while n_point < len(jobs) and jobs[n_point][0] <= cur_time:
            heapq.heappush(q, (jobs[n_point][1], jobs[n_point][0]))
            n_point += 1
    return int(sum(times) / len(times))


# print(solution2([[0, 3], [1, 9], [2, 6]]))
# print(solution2([[0, 10], [2, 10], [9, 10], [15, 2]]))
# print(solution2([[0, 10], [2, 12], [9, 19], [15, 17]]))
# print(solution2([[1000, 1000]]))
# print(solution2([[0, 1], [0, 1], [0, 1]]))
# print(solution2([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
# print(solution2([[1, 4], [7, 9], [1000, 3]]))
# print(
#     solution2(
#         [
#             [24, 10],
#             [28, 39],
#             [43, 20],
#             [37, 5],
#             [47, 22],
#             [20, 47],
#             [15, 34],
#             [15, 2],
#             [35, 43],
#             [26, 1],
#         ]
#     )
# )


# 우선 처음에 시작하는 녀석들 중에서 똑같은 시간에 시작하는 것을 대기열인 q에 넣어야 할것 아닌가?
# 어떻게? 꼭 0초에 시작하는 것이 아닐 수 있으니 처음과 2번째 그리고 그 이후의 녀석들이 같다는 정보를 얻어야지
# jobs에서 특정조건을 만족하는 녀석들만 소모시키면서 빼내는 것을 어케하지? 한녀석만 빠져나가고 그 이후에는 index가 망가져서 제대로 안된듯.
# 그렇다면 최대한 기존의 jobs을 안건드리는 방향으로? 처리했냐 못했냐는 pointer을 이용하자
# list index out of range가 계속 발생하는데... 이거 어케 처리할지는 알겠지만 좀 간편한 방법 없나?
# q가 텅비었으나 계속 jobs을 확인해야 하는 경우도 있고 끝내야 하는 경우도 있다. 어케  flag을 하나 두고 해결했다.
# if와 elif에서 코드가 중복되는데 해결할 방법이 없을까?


def solution4(jobs: list):
    q = []
    total_times = []  # sum 후에 크기로 나눠서 반환
    jobs.sort(key=lambda job: job[0])  # 요청 순서대로 정렬
    while jobs or q:
        if q:
            duration, request_time = heapq.heappop(q)
            total_times.append(duration + start_time - request_time)
            start_time = start_time + duration
        else:
            if jobs:
                start_time = jobs[0][0]
        while jobs and jobs[0][0] <= start_time:  # 우선 jobs가 있어야 빼내오니까?
            job = jobs.pop(0)
            heapq.heappush(q, (job[1], job[0]))
    return sum(total_times) // len(total_times)


print(solution4([[0, 3], [1, 9], [2, 6]]))
# 자... 테스트 케이스 하나가 잘 안되고 있다. 뭐가 문제일까?
# 오류는 시간초과이다. while문에서 문제가 발생했다고 좁히자. 1번째? 두번째? q가 있다면 반드시 뽑아낸다. 그렇다면 jobs의 존재에서 문제가 발생했다. 아 케이스 하나가 있겠다. jobs가 남아있는데 그녀석이 start_time보다 큰 경우일 것이다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다. 이 부분에서 문제 발생. 어떻게 처리하지? 현재 디스크에 아무것도 없는 상태를 어떻게 처리할까가 문제다.
# q는 비어있고 jobs는 남아있는 경우가 현재 시간이 아직 안된 것이니까 현재 시간을 맞춰준다.
