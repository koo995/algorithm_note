import sys

def solution():
    def canto(n):
        def div_conq(start, end):
            if end - start == 1: # 길이가 1이라면 그만둔다.
                return
            sub_block_size = (end - start) // 3
            for i in range(3):
                if i == 1:
                    div_conq(start + sub_block_size * i, start + sub_block_size * i + sub_block_size)
                    # 위의 범위에 녀석을 모두 공백으로 대체해야한다.
                    for idx in range(start + sub_block_size * i, start + sub_block_size * i + sub_block_size):
                        s_lst[idx] = " "
                else:
                    div_conq(start + sub_block_size * i, start + sub_block_size * i + sub_block_size)
        
        length = 3**n
        s_lst = ["-" for _ in range(length)]
        div_conq(0, length)
        print("".join(s_lst))
        
    while 1:
        try:
            num = int(input())
            canto(num)
        except:
            break

solution()
# 약간의 응용으로... "-" 이것을 쓰는 코드로 가보는것은 어떨까?