arr = [list(map(int,input().split())) for _ in range(9)]
print(arr)
max_v = -(1e9)
max_point_y = 0
max_point_x = 0
for idx_y, sub_arr in enumerate(arr):
    for idx_x, e in enumerate(sub_arr):
        if e > max_v:
            max_v = e
            max_point_y = idx_y
            max_point_x = idx_x
print(max_v)
print(max_point_y+1, max_point_x+1)
