def solution():
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    cards.sort()
    total_result = 0
    prev_sum = cards[0]
    for card in cards[1:]:
        prev_sum += card
        total_result += prev_sum
    print(total_result)


# 첫번째 풀이인 단순히 정렬해서 작은거부터 더하는 방식으로는 안되는 거엿다.

def solution2():
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())
    cards = []
    for i in range(n):
        heapq.heappush(cards, int(input()))

    result = 0

    if len(cards) == 1:
        print(result)

    else:
        for i in range(n - 1):  # 2개씩 꺼내기 떄문에 n-1
            previous = heapq.heappop(cards)
            current = heapq.heappop(cards)

            result += previous + current
            heapq.heappush(cards, previous + current)

        print(result)



solution()