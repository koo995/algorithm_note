def solution():
    import sys
    
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split())) # nums 는 최대 100만 원소는 최대 10억
    nums_dic = {}
    for num in nums:
        nums_dic[num] = 1
    nums_sorted = sorted(nums_dic.keys())
    nums_order = {num:i for i, num in enumerate(nums_sorted)}
    compressed_result = []
    for num in nums:
        order = nums_order[num]
        compressed_result.append(str(order))
    print(" ".join(compressed_result))

def solution2():
    N = int(input())
    points = list(map(int, input().split()))
    sorted_points = sorted(list(set(points)))
    point_dic = {point:idx for idx, point in enumerate(sorted_points)}
    results = []
    for point in points:
        results.append(point_dic[point])
    print(*results)
solution2()

