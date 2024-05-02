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

solution()