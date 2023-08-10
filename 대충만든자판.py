def solution(keymap, targets):
    result = [0] * len(targets)    
    # 문자의 나타난 횟수를 초기화
    char_table = {}
    for key in keymap:
        print("key:",key)
        for i in range(len(key)):
            print("char:", key[i])
            if key[i] in char_table :
                char_table[key[i]] = min(char_table[key[i]], i+1)
            else:
                char_table[key[i]] = i + 1
    print(char_table)
    # target으로 체크하자
    for i, target in enumerate(targets):
        for j in range(len(target)):
            if target[j] not in char_table:
                result[i] = -1
                break
            else:
                result[i] += char_table[target[j]]
        
        
        
    answer = result
    return answer


# keyError은 왜 나타나지? dict부분에 뭐가 문제인데...
# dict에 key가 존재 하는지 않하는지 체크는 in 으로 해야하군... 없는 녀석을가지고 dict[key] 하니까 에러뜸
# 'str' object cannot be interpreted as an integer 이건 어디서...?
# 3항 연산자를 쓰면 더 깔끔하긴 하네