def solution():
    import math
    
    N = int(input())
    garosu_lst = [int(input()) for _ in range(N)]
    distances = [garosu_lst[i+1] - garosu_lst[i] for i in range(N-1)]
    gcd = math.gcd(*distances)
    num_of_dis = (garosu_lst[-1] - garosu_lst[0]) // gcd 
    num_of_garosu = num_of_dis + 1 - len(garosu_lst)
    print(num_of_garosu)


def solution2():
    import math

    N = int(input())
    tree_points = [int(input()) for _ in range(N)]
    distances = [tree_points[i + 1] - tree_points[i] for i in range(N - 1)]
    g = math.gcd(*distances)
    print(g)
    # 그렇다면 이렇게 나온 값을 심는다면 몇개가 필요하냐?
    print((tree_points[-1] - tree_points[0]) // g - N + 1)

solution2()