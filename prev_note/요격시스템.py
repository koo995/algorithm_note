def solution(targets):
    targets.sort()
    cnt = 1
    s, e = targets[0] # 첫번째 녀석을 맞추는 미사일은 반드시 존재한다.
    for target in targets[1:]:
        n_s, n_e = target
        if n_s >= e:
            cnt += 1
            s = n_s
            e = n_e
        else:
            s = n_s
            if n_e <= e:
                e = n_e
    return cnt


def solution2(targets):
    # 일단... 개구간은 요격할 수 없다.
    targets.sort()
    s = targets[0][0]
    e = targets[0][1]
    count = 1
    for target in targets[1:]:
        if target[0] < e:
            s = target[0]
            if target[1] < e:
                e = target[1]
        elif target[0] >= e:
            count += 1
            s = target[0]
            e = target[1]
    return count



