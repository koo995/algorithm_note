def solution(sequence, k):
    subs = [] # 후보가 되는 녀석들을 여기다 집어넣는다 분류는 key= len 그중에서 첫 index가 제일 작은녀석
    window = [0,0]
    sum = 0
    while (window[1] <= len(sequence) and window[0] != len(sequence)):
        s = window[0]
        e = window[1]
        print("window: ", window)
        sum = _sum(sequence, window, k)
        if sum == k:
            subs.append(window)
            print(subs)
            s = e
            window[0] = s
            continue
        if sum > k:
            s += 1
            window[0] = s
            
        if sum < k:
            e += 1
            window[1]= e
        
    # return subs[0]

def _sum(sequence, window, k):
    result = 0
    for i in sequence[window[0]:window[1]+1]:
        result += i
    return result
    
    



# 비내림차순?
# 먼저 합이 k인 부분을 수열을 찾는데 여러개라면 길이가 짧은 녀석을 같은 길이의 짧은녀석이 여러개라면 앞쪽에 나오는 녀석을
# 순서그대로 갈것인가? 아니면 다른 방법?
# append(window)했을때 왜 기존에 넣었던 녀석도 새롭게 초기화가 되냐