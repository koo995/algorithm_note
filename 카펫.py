def find_types_of_carpet2(num):
    y, x = 0, 0
    result = set()
    for i in range(1, num):
        if num % i == 0:
            y = i
            x = num // i
            if y >= x:
                result.add((y, x))
    return result


def find_types_of_carpet(num):
    return set(
        [(i, num // i) for i in range(1, num) if (num % i == 0) and (i >= (num // i))]
    )


def check_result(y, x, brown):
    while brown > 0:
        outer_brown = (y + x - 2) * 2
        brown -= outer_brown
        if brown == 0:
            return True


def solution(brown, yellow):
    total_num = brown + yellow
    carpet_list = find_types_of_carpet(total_num)
    for carpet in carpet_list:
        if check_result(carpet[0], carpet[1], brown) == True:
            return [carpet[0], carpet[1]]


# solution(10, 2)
# solution(24, 24)
# 어짜피 모양은 직사각형이고 바깥만 주어지면... 노란색이 안에 어떻게 구성되든지 상관은 없는것 아닌가?
# 하나하나 조합을 찾아보고 그 사이에 노란색 갯수가 들어간다면 ㅇㅋ 하는걸로?
# 그냥 싹다 체크해보는 방식으로 갔는데...


def solution2(brown, yellow):
    total = brown + yellow
    # 여기서 카펫의 리스트를 어케 잡아갈까? total의 최대 갯수는 200만개이다.
    # 만약에 total이 48 이라면... 2,24인데... 사실 2도 불가능이다
    carpets = []
    for i in range(3, total):
        if total % i != 0:
            continue
        j = total // i
        if j < i:
            break
        carpets.append((j, i))

    print("carpets: ", carpets)
    for x, y in carpets:
        if 2 * (x + y) - 4 == brown:
            return [x, y]

    pass


solution2(24, 24)
