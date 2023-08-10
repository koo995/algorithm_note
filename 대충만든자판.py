def solution(keymap, targets):
    map = {}
    for key in keymap:
        for i in range(len(key)):
            k = key[i] # 이녀석은 특정 문자
            # map에 없다면 처음 넣어준다.
            if k not in map:
                map[k] = i + 1
            else: # 있다면 최소값으로 변경
                map[k] = min(map[k], i + 1)
    result = []
    for target in targets:
        flag = True
        count = 0
        for n in range(len(target)):
            s = target[n]
            if s in map:
                count += map[s]
            else: # 문자가 없다면 더이상 확인할 필요가 없다.
                result.append(-1)
                flag = False
                break
        if flag == False:
            continue
        result.append(count)
    return result


# 어디서 오류가 발생한 것이지? 정확도가 절반나오네...
# flag을 false로 했으면 true로 다시 되는 경우를 봐야지