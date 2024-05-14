def solution():
    import math
    
    N = int(input()) # N은 3의 거듭제곱 꼴이다. 3. 9. 27... 뭐... 몇번인지는 계속 3으로 나눠가면 되겠지?
    # 이야 이거.. 예전 네이버에서 하노이탑과 같다.. print 문을 이용해서 어떻게 출력해나갈지 고민해보자.
    # 한번에 프린트가 아닌... 프린트할 결과값을 어디다 저장할까?
    # 빈칸은 다른 무언가로 대체하자
    
    def star(n):
        if n == 3 :
            # 우선 여기에 2차원에 왜 슬라이싱이 들어가는지... 아아... 일단 제일 첫 녀석은 이모양이니까... 
            print_map[0][:3] = print_map[2][:3] = [1]*3
            print_map[1][:3] = [1, 0, 1]
            return
        
        a = n // 3
        star(n//3) # 여기서 재귀를 먼저 실행한다는 것이 분할정복인가... 아래서 전부 합치나 본데?
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for k in range(a):# 복사해야할 패턴의 크기로 봐도 되겠군
                    print_map[a * i + k][a * j:a * (j + 1)] = print_map[k][:a]
    
    print_map = [[0] * N for _ in range(N)] # N개 이면 N줄이 있겠지?
    star(N)
    for i in print_map :
        for j in i :
            if j :
                print('*', end = '')
            else :
                print(' ', end = '')
        print()
    

solution()