from collections import defaultdict

def solution():
    def div_conq(y, x, size):
        if size == 1:
            paper_count[M[y][x]] += 1
            return M[y][x] # size가 1이 되면 그 좌표의 -1, 0, 1의 값을 리턴한다.
        size = size // 3
        result = defaultdict(int)
        for i in range(3):
            for j in range(3):
                r = div_conq(y + size * i, x + size * j, size)
                if r is not None:
                    result[r] += 1
        keys = list(result.keys())
        if len(keys) == 1 and result[keys[0]] == 9: # 모두 똑같다면? 갯수를 세어주었던 것을 다시 빼준다. 그리고 하나로 넘긴다.
            key = keys[0]
            paper_count[key] -= 8
            return key
        
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    paper_count = [0, 0, 0]
    div_conq(0, 0, N)
    print(paper_count[-1], paper_count[0], paper_count[1], sep="\n")
    
solution()