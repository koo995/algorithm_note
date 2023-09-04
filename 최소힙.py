import heapq

N = int(input()) # (1~100000)
arr = [int(input()) for _ in range(N)]

heap = []
for e in arr:
    if e != 0:
        heapq.heappush(heap, e)
    else: # input이 0인 경우? 가장 작은 값을 출력해야지
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    
# 시간초과가 발생하네...
