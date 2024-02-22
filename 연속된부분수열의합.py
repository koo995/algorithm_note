def solution(sequence, k):
    sum_table = []
    results = []
    sum_table.append(sequence[0])  # 0인덱스는 seq[0]과 일치할 것이다.
    for s in sequence[1:]:
        sum_table.append(sum_table[-1] + s)
    s, e = 0, 0
    while e < len(sequence) and s <= e:
        sum = _sum(sum_table, s, e)
        if sum < k:
            e += 1
        elif sum > k:
            s += 1
        else:
            results.append([s, e])
            s += 1
            e += 1
    results.sort(key=lambda x: x[1] - x[0])
    return results[0]  # 짧은 순으로 정렬


def _sum(sum_table, s, e):
    return sum_table[e] - sum_table[s - 1] if s > 0 else sum_table[e]


# 비내림차순?
# 먼저 합이 k인 부분을 수열을 찾는데 여러개라면 길이가 짧은 녀석을 같은 길이의 짧은녀석이 여러개라면 앞쪽에 나오는 녀석을
# 순서그대로 갈것인가? 아니면 다른 방법?
# append(window)했을때 왜 기존에 넣었던 녀석도 새롭게 초기화가 되냐


def solution2(sequense, k):
    from collections import defaultdict

    # create accumulated sum table
    sum_table: dict = defaultdict(int)
    sum_table[0] = sequense[0]
    for idx, value in enumerate(sequense[1:], start=1):
        sum_table[idx] = sum_table[idx - 1] + value

    def _sum(s, e) -> int:
        return sum_table[e] - sum_table[s - 1] if s > 0 else sum_table[e]

    results = []

    s, e = 0, 0
    while s <= e and e < len(sequense):
        sum_value = _sum(s, e)
        if sum_value < k:
            e += 1
        elif sum_value == k:
            results.append([s, e])
            s += 1
            e += 1
        else:
            s += 1
    # sorting results by given condition
    results.sort(key=lambda x: (x[1] - x[0], x[0]))  # 기본은 작은 것이 먼저일 것이다.
    return results[0]


solution2([2, 2, 2, 2, 2], 6)


# 이런 경우는 시간 복잡도를 어떻게 계산하지?
