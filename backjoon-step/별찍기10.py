def solution():
    def star(n):
        if n == 3:
            print_map[0][:3] = print_map[2][:3] = ["*", "*" ,"*"]
            print_map[1][:3] = ["*"," ","*"]
            return
        # 만약에 아니라면은.. 더 깊숙히 들어가야지?
        star(n//3)
        inner_size = n//3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1 :
                    continue
                # 서서히 복사해 나가면서 조립해나가야한다.
                for k in range(inner_size): # k는 행의 위치를 뜻한다. 아 그리고 중복덮어씌우기가 첫번째에 발생하지만... 그냥 넘어가자.
                    print_map[inner_size * i + k][inner_size * j: inner_size * (j + 1)] = print_map[k][:3]
        
    N = int(input())
    print_map = [[" "] * N for _ in range(N)]
    star(N)
    for row in print_map:
        print("".join(row))

solution()