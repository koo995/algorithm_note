numbers_in_number_of_N_table = [[] for _ in range(10)]  # N개로 이루어진 숫자들


def return_nums_by_operations(a, b, N):
    left_list = numbers_in_number_of_N_table[a]
    right_list = numbers_in_number_of_N_table[b]
    return [
        k
        for i in left_list
        for j in right_list
        for k in operation(i, j)
        if 0 < k < 32000
    ]


def operation(i, j):
    return list(map(int, [i * j, i / j, i + j, i - j]))


def dp_update(nums, number_of_N, dp):
    for num in nums:
        if number_of_N < dp[num]:
            dp[num] = number_of_N
            numbers_in_number_of_N_table[number_of_N].append(num)


def solution(N, number):
    max_n = 32001
    dp = [10] * max_n
    for i in range(1, 10):
        n = int(str(N) * i)
        if n < max_n:
            dp[n] = i
            numbers_in_number_of_N_table[i].append(n)
    for number_of_N in range(2, 9):
        sub_n = number_of_N
        while sub_n > 0:
            sub_n -= 1
            opposite_sub_n = number_of_N - sub_n
            if sub_n > 0:
                result_nums = return_nums_by_operations(sub_n, opposite_sub_n, N)
                dp_update(result_nums, number_of_N, dp)
    return dp[number] if dp[number] <= 8 else -1


print(solution(5, 12))
# print(solution(2, 11))
# print(solution(6, 5))
# print(solution(2, 11))
# "/" 연산은 float을 반환하나 보네
# 무한 루프에 빠지는 이유는 뭐지? 동전의 갯수가 업데이트가 안되는 구나
# 나머지는 무시한다는데...
# dp문제인 만큼 어떻게 케이스를 나눠야하냐가 중요한 것이였어... dp라 해야할지... 테이블을 하나더 구성해서 정보를 저장하고...
# 어쨋든 dp문제는 어떻게 문제를 나눌것이냐가 중요한데 그 부분에 있어서 더 자세히 나누지 못했어 2개짜리 2개짜리 조합으로 4개짜리 조합이 될 수 있었으니...
