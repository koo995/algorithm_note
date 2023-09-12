from string import ascii_uppercase
letters = {}
for idx, a in enumerate(list(ascii_uppercase)):
    letters[a] = idx+10

N, B = (lambda x: (x[0], int(x[1])))(input().split())
result = 0
for idx, s in enumerate(N):
    # n이 정수가 가능하다면 어떻게 처리하지?
    if s.isdigit() :
        result += int(s) * pow(B, (len(N)-idx-1))
    else:
        result += letters[s] * pow(B, (len(N)-idx-1))

print(result)