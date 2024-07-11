def solution(phone_book: list):
    dict = {}
    answer = True
    # 모든 번호에 대해서 해시로 저장
    for i in phone_book:
        dict[i] = 0  # value값은 상관이 없다 key값에서 충돌이 나타나는지로 체크하기 위함
    for num in phone_book:
        s = ""
        for sub_num in num:
            s += sub_num
            # 여기 이 부분 되게 중요하다... dic에서는 in으로 찾는 것이 시간복잡도가 1에 해당된다.
            if s in dict and s != num:  # 자기자신은 해당되면 안되지
                answer = False
                return answer

    return answer


def solution2(phone_book: list):
    from collections import defaultdict

    phone_book.sort(key=lambda x: len(x))
    print("phone_book: ", phone_book)
    dic = defaultdict(str)
    for phone_num in phone_book:
        dic[phone_num] = 1
    for num in phone_book:
        s = ""
        for sub_num in num:
            s += sub_num
            if s in dic:
                return False
    return True


def solution3(phone_book: list):
    def check_prefix(num1, num2):
        s1 = len(num1)
        s2 = len(num2)
        if s1 < s2 and num2[:s1] == num1:
            return True
        return False

    phone_book.sort()
    start = 0
    size = len(phone_book)
    while start + 1 < size:
        prev_number = phone_book[start]
        next_number = phone_book[start + 1]
        if check_prefix(prev_number, next_number):
            return False
        start += 1
    return True
