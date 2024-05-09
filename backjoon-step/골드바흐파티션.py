import math
import sys

def solution():
    def check_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # 소수들을 제너레이터를 이용할까?
    def find_gold_bach_part_num(n) -> int:
        # n이 최대 100만인데... 여기서 50만이 소요될수있다.
        # n = a + b 이고 a와 b가 소수라면 그것을 더한 것은? a = n - b 도 소수란 말이다. 
        count = 0
        for a in prime_nums:
            b = n - a
            if a > b:
                break
            if check_prime(b):
                count += 1
        return count
    
    T = int(sys.stdin.readline())
    test_cases = [int(sys.stdin.readline()) for _ in range(T)]
    prime_nums = [i for i in range(2, int(1e6)) if check_prime(i)]
    
    for num in test_cases:
        # num이 골드바흐파티션의 갯수를 구한다
        print(find_gold_bach_part_num(num))


def solution2():
    T = int(sys.stdin.readline())
    test_cases = [int(sys.stdin.readline()) for _ in range(T)]
    # 소수 초기화
    MAX = int(1e6) + 1
    prime_nums = []
    prime_check = [1] * MAX
    prime_check[0] = 0
    prime_check[1] = 0
    for n in range(2, MAX):
        if prime_check[n] == 0:
            continue
        prime_nums.append(n)
        for i in range(2, (MAX // n) + 1):
            if n * i < MAX:
                prime_check[n * i] = 0
                
    for test_num in test_cases:
        # 이제 이 테케들이 소수의 합으로 나눠지는지 확인해야겠구만...
        count = 0
        for prime_num1 in prime_nums:
            prime_num2 = test_num - prime_num1
            if prime_num1 > prime_num2:
                break
            if prime_check[prime_num2]:
                count += 1
        print(count)

solution2()

# 역시 그냥 이러한 풀이는 시간초과를 발생시키네...
# 100만 까지 모든수에 대해서 프라임이냐 아니냐를 판단하는것은 너무 오래 걸린다.
# 그렇다면 모든 수를 구해놓고 프라임인지 아닌지 체크해 놓는것이 어떤가로 가는게 좋아보인다...?