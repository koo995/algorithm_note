def solution(text, skip, index):
    def rou(num):
        if num > ord('z'): # 124라면 b가 되어야 한다.
            num = 96 + num % ord('z')
        return num
    # a는 아스키코드로 97 z는 아스키코드로 122
    result = ""
    skip = [ord(s) for s in skip ]
    for s in text:
        asci_s = ord(s)
        for _ in range(index):
            asci_s = rou(asci_s + 1)
            if asci_s in skip:
                while(asci_s in skip):
                    asci_s = rou(asci_s + 1)
        result += chr(asci_s)
    return result


# print(solution("z", "a", 1))
print(solution("bcdefghijklmnopqrstuvwxyz", "a", 1))
print(solution("klmnopqrstuvwxyz", "abcdefghij", 20))

# 순환하도록 하는 방식이 쉽지 않네 97과 122사이를
# 문제는 연속된 녀석들이 skip에 포함된 경우구나
# from string import lowercase 하면 소문자로 구성된 알파벳배열을 얻을수 있구나.
# 플러스가 되어서 변환된 녀석이 skip에 포함되었는지 확인해야 하는데... skip안에는 97-122만 들어있으니 문제가 발생