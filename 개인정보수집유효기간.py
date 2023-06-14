term_table = {}
def solution(today, terms, privacies):
    result = []
    # 약관 종류를 dict으로 초기화
    for term in terms:
        t_name, exp = term.split()
        term_table[t_name] = int(exp)
        
    # 프라이버시 정보를 체크
    for i , privacy in enumerate(privacies):
        date_get, name = privacy.split(" ")
        if True == check(today, date_get, term_table[name]):
            result.append(i+1)
    
    answer = result
    return answer

def check(today, date_get, exp):
    # 현재의 날짜 2000년 이후의 일수로 나타내보자
    t_y, t_m, t_d = map(int,today.split("."))
    y, m, d = map(int, date_get.split("."))
    t_days = (t_y-2000) * 28 * 12 + t_m * 28 + t_d
    print("today 일수: ", t_days)
    date_days = (y-2000) * 28 * 12 + m * 28 + d
    exp_days = date_days + 28 * exp -1
    print(" 만기 일수: ", exp_days)
    if t_days > exp_days:
        return True
    
    


# 여러 테이블을 어떻게 처리할까? 딕셔너리?
# 파기는 보관 다음날
# 유효기간은 xx달이니까 %12을 해서 나머지 몫을 따져야할듯
# 만기날짜계산에서 뭔가 잘못되었는데...
# 11//12가 왜 5로 뜨냐... 아 더하기 먼저할땐 괄호를...
# 28일까지란 조건을 고려해야지
# 이런건 실생활에서 매우 유용할 내용인데
# 이런건 일 수로 풀어서 보는게 좋을려나 날짜 계산에 나누기 몫 그런건 안좋은듯
