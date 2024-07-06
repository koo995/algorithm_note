n = int(input())
containers = list(map(int, input().split()))

max_list = [0] * 100
max_list[0] = containers[0]
max_list[1] = max(containers[0], containers[1])

for i in range(2, n):
    max_value = int(max(max_list[i-1], max_list[i-2] + containers[i]))
    max_list[i] = max_value

print(max_list[n-1])
# 한가지 특이점. 창고를 터는데는 갯수 제한이 없다.
# 점화식을 어떻게 코드로 만들까? 그냥 그대로 만드는데... 0번 또는 1번을 반복문안에 조건문으로 넣을까 하다 그냥 바깥에서 초기화함... 이래도 되나
# 답지도 이렇군