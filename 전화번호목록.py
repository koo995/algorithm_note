import random
def solutuion(phone_book:list):
    dict = {}
    answer = True
    # 모든 번호에 대해서 해시로 저장
    for i in phone_book:
        dict[i] = random.randint() # value값은 상관이 없다 key값에서 충돌이 나타나는지로 체크하기 위함
    for num in phone_book:
        s = ""
        for sub_num in num:
            s += sub_num
            if s in dict:
                answer = False
                return answer
        
    return answer
    