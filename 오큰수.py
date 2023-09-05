from collections import deque

N = int(input()) # 1~1e6
arr = list(map(int, input().split())) # 각 원소의 크기도 100만 까지
answer = [-1] * (N)
stack = deque()
stack.append(0)
for idx in range(1,N):
    while stack and arr[idx] > arr[stack[-1]]:
        answer[stack.pop()] = arr[idx]
    stack.append(idx)    

for i in answer:
    print(i, end=" ")
        
# 오큰수를 어떻게 구할까?
# 시간 초과가 발생했다.
# 어떻게 해결할까? 제한시간은 1초이며 100만의 길이에 겨우 10만 곱하기가 가능한 처지가
# 정렬 알고리즘을 쓰면서 바뀌기만 하면 기록할까?
# 원소 하나하나에 대해서 확인하며 오른쪽 녀석들을 살펴보는것은 시간이 안된다. 

# 이 방식의 시간 복잡도를 어떻게 계산해야 할까
# 어쨋든 이러한 인덱스를 stack에 넣는것은 시간을 크게 줄일 수 잇구나