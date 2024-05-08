def solution():
    import math
    
    N = int(input())
    garosu_lst = [int(input()) for _ in range(N)]
    distances = [garosu_lst[i+1] - garosu_lst[i] for i in range(N-1)]
    gcd = math.gcd(*distances)
    num_of_dis = (garosu_lst[-1] - garosu_lst[0]) // gcd 
    num_of_garosu = num_of_dis + 1 - len(garosu_lst)
    print(num_of_garosu)

solution()