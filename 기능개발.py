from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque() 
    for n in range(1,100): # 이건 일수를 뜻함
        # 모든 프로세스들에 대해서 작업분을 반영함
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        print(f"progress {n}쨋날",progresses)
        while(progresses and progresses[0] >= 100):
            q.append(progresses.pop(0))
            speeds.pop(0)
            print("for문 안에서", progresses)
        if q :
            answer.append(len(q))
            q.clear()
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([90, 98, 97, 96, 98], [1, 1, 1, 1 ,1]))
print(solution([1,1,50], [100, 2,1]))

# 문제가 생긴 부분은... speeds에서 pop을 안해줬더니 progrees에 순서가 다른 스피드가 적용되었어...