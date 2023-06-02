x = int(input())


result = 0
data = [0] * 30001
data[1] = 0
data[2] = 1
for i in range(3, x + 1): #이것을 굳이 30001까지 돌릴 필요는 없지
    buffer = []
    if i % 5 == 0:
        buffer.append(data[i//5])
    if i % 3 == 0:
        buffer.append(data[i//3])
    if i % 2 == 0:
        buffer.append(data[i//2])
    buffer.append(data[i - 1])
    buffer.sort()
    print(buffer)
    data[i] = buffer[0] + 1
    print(f"data[{i}]: ", data[i])

print(data[x])
#처음에 greedy하게 가야하는 문제인가 생각했는데... 그러면 안될 이유가 보이는군 순서가 결과에 영향을 미쳐
# 이것이 다아니막 프로그래밍 바텀업이라는것을 어떻게 체크할까? 문제의 예시를 보다가 어느정도 깨닳아야 할까?
# 조건문 안에 and data[i//5]와 같은 조건을 걸어서 문제가 되었어
# 이렇게 버퍼를 만들어서 분류하는 것은... 좀더 시간이 많이 걸릴까? 어짜피 sort는 4개만 분류하는데 상관없을듯하고...
# 책에서는 min(,)연산을 수행해서 매번 비교하더라