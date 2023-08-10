def solution(n, m, sections):
    s = sections[0]
    e = s + m -1 # 단순히 더하기만 하기에는 본인도 포하해야징
    count = 1
    for section in sections[1:]:
        if section > e:
            count += 1
            s = section
            e = s + m -1
    return count