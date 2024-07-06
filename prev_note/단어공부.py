from collections import Counter

input_str = [s.upper() for s in list(input())]
c = Counter(input_str)
l = c.most_common()
l.sort(key=lambda x:x[1], reverse=True)
if len(l) > 1 and l[1] and l[1][1] == l[0][1]:
    print("?")
else:
    print(l[0][0])
    
# 어디서 인덱스 에러가 뜨는 거지?
# 