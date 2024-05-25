def solution():
    # 10 + 20 - 30 + 50 + 20 - 30 여기서 괄호를 쳐서 최소로 만들려면 어떻게 하지?
    # 괄호를 친다는 말은.. 연산을 먼저 수행한다는 것인데.. 최대한 - 연산의 결과가 커지도록 하는 것이 중요하겠다.
    # 이제 중요한 것은 어떻게 파싱해 나갈까가 문제다.
    # 사실상 생각해보니까... 마이너스가 하나라도 있으면 그냥 전부다... 마이너스로 넣어버리면 되네....
    S = input()
    pointer = 0
    num_lst = []
    operation_lst = []
    while pointer < len(S):
        start_point = pointer
        while pointer < len(S) and S[pointer].isnumeric():
            pointer += 1
        end_pointer = pointer
        num_lst.append(int(S[start_point:end_pointer]))
        if end_pointer < len(S):
            operation_lst.append(S[end_pointer])
        pointer += 1
    result = [num_lst[0]]
    minus_flag = False
    for idx, operation in enumerate(operation_lst, start = 1):
        if operation == '-':
            minus_flag = True
        if not minus_flag:
            result.append(num_lst[idx])
        else:
            result.append(-1 * num_lst[idx])
    print(sum(result))
        
        
solution()