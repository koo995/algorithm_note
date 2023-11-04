x = int(input())

match = False
n = 1
while match == False:
    s_1 = int((n - 1) * (n) / 2)
    s = int(n * (n + 1) / 2)
    if x <= s:
        diff = x - s_1 - 1 if n % 2 == 0 else s - x  # 첫 라인부터 diff번째 라는 것
        a = 1 + diff
        b = n - diff
        print("n: ", n)
        print("a, b: ", a, b)
        print("diff: ", diff)
        match = True
        print("s: ", s)
        print("s_1: ", s_1)
    n += 1
print(f"{a}/{b}")

# 처음에 그냥 어떻게 해야할지 감이 안잡혔지만... 등차수열의 합이 갑자기 생각이 났어... 양끝쪽이 서로 대칭이라는 점에서 힌트를 얻었지
