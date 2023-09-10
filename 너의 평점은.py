grade = {"A+":4.5, 
         "A0":4.0,
         "B+":3.5,
         "B0":3.0,
         "C+":2.5,
         "C0":2.0,
         "D+":1.5,
         "D0":1.0,
         "F":0.0}
# 추가로 P/F 등급에서 P는 제외하기
# 정답과의 절대오차 또는 상대오차가 \(10^{-4}\) 이하이면 정답으로 인정 3.3이상이여야함
scores = [(lambda x:[float(x[1]), x[2]])(input().split()) for _ in range(20)]
# [[3.0, 'A+'], [3.0, 'A+'], [3.0, 'A0'], [3.0, 'A+'], [3.0, 'A+'], [3.0, 'B0'], [3.0, 'A0'], [3.0, 'B0'], [3.0, 'B0'], [3.0, 'C+'], [3.0, 'B0'], [4.0, 'A+'], [3.0, 'B+'], [3.0, 'C0'], [3.0, 'D+'], [3.0, 'C+'], [3.0, 'B0'], [3.0, 'B+'], [3.0, 'D0'], [4.0, 'P']]
total_socre = float(0)
total_grade = 0
for score in scores:
    if score[1] == "P":
        continue
    total_socre += score[0] * grade[score[1]]
    total_grade += score[0]
print("t_g: ", total_grade)
print("t_s:", total_socre)
print("{:.6f}".format(total_socre/(total_grade)))