def solution(name, yearning, photos):
    result = []
    dic= {n:yearning[idx] for idx, n in enumerate(name) } # 이렇게 해봤자 시간 복잡도 100이 최대?
    print(dic)
    for photo in photos:
        sub_result = 0
        for p_name in photo:
            if p_name in dic:
                sub_result += dic[p_name]
        result.append(sub_result)
    return result