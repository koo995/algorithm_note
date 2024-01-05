def solution(progresses, speeds):
    from collections import deque

    answer = []
    q = deque()
    for n in range(1, 100):  # 이건 일수를 뜻함
        # 모든 프로세스들에 대해서 작업분을 반영함
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            q.append(progresses.pop(0))
            speeds.pop(0)
        if q:
            answer.append(len(q))
            q.clear()
    return answer


# 뭐... 이게 더 빠르긴 하네
def solution2(progresses: list, speeds):
    import math

    count = 0
    answer = []
    day = 0
    while progresses:
        if (progresses[0] + day * speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:  # 100 보다 작다면... 100 이 되도록 해야지?
            day = math.ceil((100 - progresses[0]) / speeds[0])
            if count != 0:
                answer.append(count)
            count = 0
    answer.append(count)
    return answer


print(solution2([93, 30, 55], [1, 30, 5]))
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution2([1, 1, 50], [100, 2, 1]))

# 문제가 생긴 부분은... speeds에서 pop을 안해줬더니 progrees에 순서가 다른 스피드가 적용되었어...
