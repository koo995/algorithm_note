# 시각
n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = list(str(h)) + list(str(m)) + list(str(s))
            print(time)
            if '3' in time:
                count +=1
            
print(count)
#참고 python 의 문법은 "sdlfkjsldkjf" 여기서 's'가 있는지 없는지 판별이 가능하다. 굳이 list로 표현할 필요가 없다.