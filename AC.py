from collections import deque

T = int(input())
cases = [[input() for _ in range(3)]  for _ in range(T)]

for case in cases:
    case = [case[0], int(case[1]), list(map(int,case[2][1:-1].split(","))) if len(case[2]) > 2 else []]
    functions = case[0]
    n = case[1]
    arr = deque(case[2])
    flag = True
    reverse = False
    R_count = 0
    
    for func in functions:
        if func == "D": # 버리기
            if len(arr) != 0 :
                if reverse == False:
                    arr.popleft() # 인덱스를 지정해서 그렇구나...
                else:
                    arr.pop()
            else:
                print("error")
                flag = False
                break
            
        else: # func == "R" 뒤집기
            R_count += 1
            reverse = True if R_count % 2 != 0 else False
    if flag == False:
        continue
    
    result = list(arr)
    if R_count % 2 != 0:
        result.reverse()
    print(result)


# 시간 초과가 발생하네... 뒤집기에서 문제가 생기는 것 같아.
# 어디서 뭘 어떻게 줄여야 하지? 뒤집기에서 로그연산을 하면 시간복잡도가 딱 알맞는듯
# boolean 변수로 R의 갯수에 따라 앞에서 뒤에서 pop() 하는 방식을 썼는데...
# 어떤 케이스에서 틀린걸까?