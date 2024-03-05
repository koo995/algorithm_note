def solution(citations: list):
    h = 0
    citations.sort()
    print("citations: ", citations)
    for pre_h in range(len(citations)):  # pre_h가 h값의 후보라 하자.
        print("pre_h: ", pre_h)
        count = 0
        for idx, citation in enumerate(citations):
            # 전체 인용된 논문들 중에서 pre_h보다 크거나 같은 수를 세어준다.
            if citation >= pre_h:
                count += 1
        print("count: ", count)
        if count >= pre_h and (
            (citations[len(citations) - 1 - count] <= pre_h)
            or (count >= len(citations))
        ):  # 나머지 논문중에서 제일 큰 녀석 :
            h = max(h, pre_h)
            print("h값 변경되었어.: ", h)

    return h


# 이상과 이하를 잘 살펴봐야 겠네...
# 뭐가 틀린거지?
# 어쨋든 이론상 천만까지 연산은 가능하니 모든 케이스를 다 살펴보는 것도 가능하다.
# 근데 그렇게 풀면 정렬과 어떤 관련...? 아하 h의 값은 전체 논문의 수를 넘길수가 없네
# 이 문제는... 어찌보면 해란거 그대로 구현하기만 하면 되는 문제 같다
# 하나의 케이스가 문제다. [3,4]인 경우다. 어떻게 하면 조건을 조금 더 깔끔하게 할 수 있을까
# 저 조건... 너무 케이스에 맞춘 어거지 조건 같은데...


def solution2(citations):
    citations.sort(reverse=True)
    enumerated = list(enumerate(citations, start=1))
    print("enumerated: ", enumerated)
    result = list(map(min, enumerated))
    print("result: ", result)
    answer = max(result)
    return answer


def solution3(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


print(solution2([3, 0, 6, 1, 5, 0, 2, 2, 2, 4, 5, 64, 4, 4, 5]))

# 어라 저런 문법이 있다고...?
# enumerate에 매개변수로 start을 줄 수 있구나


def solution4(citations):
    # 어쨋든 완전탐색을 가도... 천만 정도니까... 할만한데?
    h_index = 0
    n = len(citations)
    for h in range(int(1e4)):
        upper_count = 0
        lower_count = 0
        for citation in citations:
            if citation >= h:
                upper_count += 1
            else:
                lower_count += 1
        if upper_count >= h and lower_count <= h:
            h_index = max(h_index, h)
    return h_index


# 예전에는 이문제를 어떻게 가야할지도 모르겠던데... 지금은 그래도 그냥 모두 탐색해도 될것같다는 생각이 들었다..
