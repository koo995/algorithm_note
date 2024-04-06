def solution(lottos, win_nums):
    from itertools import combinations
    
    def num_generator(lottos):
        for i in range(1, 46):
            if i not in lottos:
                yield i
    
    
    win_count = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    # 기존에는 몇개가 일치하는지 세어보자.
    matching_count = 0
    max_count = 0
    min_count = 6
    for num in lottos:
        if num in win_nums:
            matching_count += 1
    zero_count = lottos.count(0)
    num_comb_set = set(combinations(num_generator(lottos), zero_count))
    for num_comb in num_comb_set:
        temp = matching_count
        for num in num_comb:
            if num in win_nums:
                temp += 1
        max_count = max(max_count, temp)
        min_count = min(min_count, temp)
    print("max: ", max_count, "min: ", min_count)
    return [win_count[max_count], win_count[min_count]]


print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))