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

