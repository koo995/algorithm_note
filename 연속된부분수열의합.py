def solution(sequence, k):
    sum_table = []
    results = []
    sum_table.append(sequence[0]) # 0인덱스는 seq[0]과 일치할 것이다.
    for s in sequence[1:]:
        sum_table.append(sum_table[-1] + s)
    s, e = 0, 0
    while (e < len(sequence) and s<=e):
        sum = _sum(sum_table, s, e)
        if sum < k: e += 1
        elif sum > k: s += 1
        else: 
            results.append([s,e])
            s += 1
            e += 1
    results.sort(key=lambda x: x[1]-x[0])
    return results[0] # 짧은 순으로 정렬

def _sum(sum_table, s, e):
    return sum_table[e] - sum_table[s-1] if s > 0 else sum_table[e]

    
solution([1,2,3,4,5], 7)


# 비내림차순?
# 먼저 합이 k인 부분을 수열을 찾는데 여러개라면 길이가 짧은 녀석을 같은 길이의 짧은녀석이 여러개라면 앞쪽에 나오는 녀석을
# 순서그대로 갈것인가? 아니면 다른 방법?
# append(window)했을때 왜 기존에 넣었던 녀석도 새롭게 초기화가 되냐