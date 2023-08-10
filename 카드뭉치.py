def solution(cards1, cards2, goal):
    result = "Yes"
    for g_word in goal:
        if cards1 and g_word == cards1[0]:
            cards1.pop(0)
        elif cards2 and g_word == cards2[0]:
            cards2.pop(0)
        else:
            result = "No"
            break
    return result
        
        
# list 에서는 index 을 찾는 메소드에서 없으면 오류가뜨네
# 그냥 in으로 존재여부 확인해야 할듯
# list index_ out of range는 어디서 뜨는거지?
# list가 빈리스트가 되었을때 index로 참조할려면 에러가 뜨는거 같아.
# and 조건을 쓸때 문장의 길이를 먼저 확인하는 방법과 같이 조건을 앞에 달아주면 뒤에 오류는 안발생해
# a and b 연산일때 a가 틀리면 b는 확인을 안하나봐
# index 화살표를 하나 두고 한칸씩 움직이는게 좋군
# goal의 원소들이 card에 들어가 있고 순서를 유지하지만 처음부터 나오는게 아니기 때문에 No를 반환하셔야 합니다.