import sys
input = sys.stdin.readline

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]  # (y, x, color)

# 모든 점의 y좌표만 추출 후 중복 제거 + 정렬
unique_y = sorted(set(p[0] for p in points))

INF = 10**18
answer = INF

# 각 y좌표 쌍 (y_low, y_high)에 대해
for i in range(len(unique_y)):
    for j in range(i, len(unique_y)):
        y_low = unique_y[i]
        y_high = unique_y[j]

        # y_low <= y <= y_high 범위에 포함되는 점들만 추림
        candidate = []
        for (y, x, c) in points:
            if y_low <= y <= y_high:
                candidate.append((x, c))

        # x좌표 기준 정렬
        candidate.sort(key=lambda x_c: x_c[0])

        # 슬라이딩 윈도우로 K가지 색을 모두 만족하는 최소 x구간 탐색
        color_count = [0]*(K+1)  # 색이 1..K라 가정
        have_color = 0  # 현재 윈도우 안에 몇 개의 색깔이 들어있는지
        left = 0

        # 오른쪽 포인터 right를 이동시키면서
        for right in range(len(candidate)):
            x_right, c_right = candidate[right]
            if color_count[c_right] == 0:
                have_color += 1
            color_count[c_right] += 1

            # 만약 K가지 색을 모두 포함(have_color == K)하게 되면
            # 더 줄일 수 있는지 left를 앞으로 당겨 봄
            while have_color == K:
                x_left, c_left = candidate[left]
                # 현재 구간으로부터의 면적 계산 (세로 * 가로)
                width = (x_right - x_left)
                height = (y_high - y_low)
                area = width * height
                answer = min(answer, area)

                # 왼쪽 색을 한 칸 줄이면서 윈도우 축소
                color_count[c_left] -= 1
                if color_count[c_left] == 0:
                    have_color -= 1
                left += 1

# 만약 찾지 못했다면 (모든 색을 담는 사각형이 불가능하면) 적절히 처리
if answer == INF:
    print(0)  # 문제 조건에 맞춰서 에러 처리 or 0 or 등등
else:
    print(answer)
