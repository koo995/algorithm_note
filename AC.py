from collections import deque

T = int(input())
cases = [[input() for _ in range(3)]  for _ in range(T)]
# [['RDD', '4', '[1,2,3,4]'], ['DD', '1', '[42]'], ['RRD', '6', '[1,1,2,3,5,8]'], ['D', '0', '[]']]

for case in cases:
    case = [case[0], int(case[1]), list(map(int,case[2][1:-1].split(","))) if len(case[2]) > 2 else []]
    functions = case[0]
    n = case[1]
    arr = deque(case[2])
    flag = True
    
    for func in functions:
        if func == "D": # 버리기
            if len(arr) != 0 :
                arr.popleft() # 인덱스를 지정해서 그렇구나...
            else:
                print("error")
                flag = False
                break
            # print("버린 arr: ", arr)
            
        else: # func == "R" 뒤집기
            arr = deque([arr.pop() for _ in range(len(arr))])
            # print("뒤집은 arr: ", arr)
    if flag == False:
        continue
    
    print(list(arr))


# 시간 초과가 발생하네... 뒤집기에서 문제가 생기는 것 같아.
# 어디서 뭘 어떻게 줄여야 하지? 뒤집기에서 로그연산을 하면 시간복잡도가 딱 알맞는듯