def solution():
    import math
    
    N = int(input()) # N은 3의 거듭제곱 꼴이다. 3. 9. 27... 뭐... 몇번인지는 계속 3으로 나눠가면 되겠지?
    # 이야 이거.. 예전 네이버에서 하노이탑과 같다.. print 문을 이용해서 어떻게 출력해나갈지 고민해보자.
    # 한번에 프린트가 아닌... 프린트할 결과값을 어디다 저장할까?
    # 빈칸은 다른 무언가로 대체하자
    
    def replace_empty(n):
        if n == 1: # 가운데에 비는것을 어떻게 처리할까? 그리고 높이도 어떻게 처리할까?
            # 가운데를 비운다를 어떻게 가지?
            # 이 위치의 녀석을 공백으로 환한다...
            pass
        # 만약에 N 이 들어온다면...
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # 이 부분이 완전히 비워져야하는데?
                    replace_empty(n//3)
        
        pass
    print_stack = [[" "] * N for _ in range(N)] # N개 이면 N줄이 있겠지?
    print(print_stack)
    replace_empty(N)

solution()