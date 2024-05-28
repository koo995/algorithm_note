from collections import defaultdict

def solution():
    def div_conq(y, x, size):
        if size == 1:
            return str(M[y][x]) # size가 1이 되면 그 좌표의 -1, 0, 1의 값을 리턴한다.
        size = size // 3
        result = defaultdict(int)
        for i in range(3):
            for j in range(3):
                r = div_conq(y + size * i, x + size * j, size)
                result[r] += 1
        keys = list(result.keys())
        if len(keys) == 1: # 모두 똑같다면?
            key = keys[0]
            return str(key)
                # 9등분한 값들을 깊이 들어간다음.. 나와서 이제 정복해나가야 하는데 어떻게 하지?
                # 9개의 결과가 모두 같다면 하나로 퉁치고 카운팅한다. 하지만 하나라도 다르다면? 각자의 갯수로 카운팅한다.
                # 어쨋든 각 재귀함수의 결과를 한번에 고려할 수 있어야 한다. 방법 1. 리스트에 결과를 저장한다?
        else: # 한녀석이라도 다르거나, 이미 종이수를 체크한 경우
            for key in result.keys():
                if key == "N":
                    continue
                paper_count[key] += result[key]
            return "N"
        
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    paper_count = {"-1": 0, "1": 0, "0": 0}
    r = div_conq(0, 0, N)
    if r != "N":
        paper_count[r] += 1
    print(paper_count["-1"], paper_count["0"], paper_count["1"], sep="\n")
    

solution()