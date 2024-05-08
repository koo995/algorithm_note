def solution():
    def print_prime_num(n):
        import math
        
        if n == 0 or n == 1:
            print(2)
        else:
            # n 보다 큰 수들에 대해서 약수들을 찾아가야 한다. 그 중에서 
            # n에 대해서 약수를 찾는데... 
            find_prime = False
            while not find_prime :
                find_prime = True
                # n의 약수를 찾는다. 가 아니라 n이 소수인지 아닌지 판단하는 것이지
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        find_prime = False
                        n += 1
                        break
            print(n)
    
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]
    for test_case in test_cases:
        print_prime_num(test_case)

solution()