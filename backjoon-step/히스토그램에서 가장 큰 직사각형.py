import math

def solution():
    while 1:
        i = input()
        if i == "0":
            break
        N, *heights = map(int, i.split())
        stack = [(0, heights[0])]
        max_volume = -math.inf
        if N == 1:
            v, h = stack.pop()
            print(h)
        else:
            for v2, height in enumerate(heights[1:], start=1):
                if stack and stack[-1][1] > height: # 작아진다면 최대 값을 업데이트 해줘야 겠지?
                    while stack and stack[-1][1] > height: # 내려가는 경우 넓이를 어떻게 하지가 문제구나.. 어쨋든 스택안에 있는 녀석들 너비로 활용해야 하고.. 그 녀석은 현시점의 Height 보다 값이 작을 수 있다.
                        _, max_h = stack.pop()
                        v1 = 1 # 스택이 없다면 그냥 이것을 쓴다.
                        if stack:
                            v1 = stack[-1][0] + 1
                        max_volume = max(max_volume, max_h * (v2 - v1))                    
                stack.append((v2, height))
            while stack:
                # stack에 여전히 남아있다면? 큰 순서대로 줄줄이 있을것이니까... 넓이를 어떻게 하지?
                _, max_h = stack.pop()
                v1 = 1
                if stack:
                    v1 = stack[-1][0] + 1
                max_volume = max(max_volume, max_h * (N - v1))
            print(max_volume)
                


def solution2():
    import math

    while True:
        i = input()
        if i == "0":
            break
        N, *heights = map(int, i.split())

        # 스택과 최대 직사각형 넓이를 저장할 변수를 초기화합니다.
        stack = []
        max_result = -math.inf

        for v2, height in enumerate(heights, start=1):
            # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작으면
            if stack and stack[-1][1] > height:
                while stack and stack[-1][1] > height:  # 스택에서 빼내며 최대 직사각형 넓이를 계산합니다.
                    _, stack_height = stack.pop()
                    v1 = 1
                    if stack:
                        v1 = stack[-1][0]+1
                    result = (v2 - v1) * stack_height
                    max_result = max(result, max_result) # 최대값 갱신
                    # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산합니다.
            stack.append((v2, height))  # 스택에 현재 막대기를 추가합니다.

        # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산합니다.
        while stack:
            _, stack_height = stack.pop()
            v1 = 1
            if stack:
                v1 = stack[-1][0]+1
            result = (N+1 - v1) * stack_height
            max_result = max(result, max_result) # 최대값 갱신

        # 최대 직사각형 넓이를 출력합니다.
        print(max_result)
solution2()