def solution(routes):
    routes.sort(key=lambda x: x[0])
    camera_point = routes[0][1]  # 제일 첫번째 차량의 나간 지점.
    total_camera_num = 1
    for route in routes[1:]:
        if camera_point < route[0]:
            camera_point = route[1]
            total_camera_num += 1
        if route[1] < camera_point:
            camera_point = route[1]

    return total_camera_num


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
