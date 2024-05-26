def solution():
    N = int(input())
    road_length = list(map(int, input().split()))
    node_price = list(map(int, input().split()))
    visited = [0] * N
    total_cost = 0
    for i in range(N - 1):
        if visited[i]:
            continue
        visited[i] = 1
        length = road_length[i]
        price = node_price[i]
        tmp = i + 1
        while tmp < N - 1 and node_price[i] < node_price[tmp]:
            # 다음 녀석이 더 비싸다면.. 최대한 그 거리까지 여기서 다 채운다
            length += road_length[tmp]
            visited[tmp] = 1
            tmp += 1
        total_cost += length * price
    print(total_cost)


solution()