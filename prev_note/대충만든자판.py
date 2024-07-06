def solution(keymap, targets):
    map = {}
    for key in keymap:
        for i, s in enumerate(key):
            map[s] = min(map[s], i + 1) if s in map else i + 1
    result = []
    for target in targets:
        flag = True
        count = 0
        for s in target:
            if s in map:
                count += map[s]
            else:  # 문자가 없다면 더이상 확인할 필요가 없다.
                result.append(-1)
                flag = False
                break
        if flag == False:
            continue
        result.append(count)
    return result


def solution1(keymap, targets):
    from collections import defaultdict

    answer = []
    keydic = defaultdict(int)
    for key in keymap:
        for i, c in enumerate(key, start=1):
            keydic[c] = i if c not in keydic else min(i, keydic[c])
    for target in targets:
        tmp_count = 0
        for ch in target:
            if ch not in keydic:
                tmp_count = -1
                break
            tmp_count += keydic[ch]
        answer.append(tmp_count)
    return answer


print(solution1(["ABACD", "BCEFD"], ["ABCD", "AABB"]))

# 어디서 오류가 발생한 것이지? 정확도가 절반나오네...
# flag을 false로 했으면 true로 다시 되는 경우를 봐야지
