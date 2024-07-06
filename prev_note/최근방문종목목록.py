from collections import deque
import copy 

class people():
    def __init__(self):
        self.recent_t = deque()
        self.back_t = deque()
        self.forward_t = deque()
    
    def direct(self, num): # 문자열로 받음
        if self.recent_t:
            temp = copy.deepcopy(self.recent_t)
            self.back_t.appendleft(temp.popleft())
        self.forward_t.clear()
        if num not in list(self.recent_t): # 여기서 중복된것을 제거하니까
            self.recent_t.appendleft(num)
            
    def back(self):
        if self.back_t:
            temp = copy.deepcopy(self.recent_t)
            self.forward_t.appendleft(temp.popleft())
            self.recent_t.appendleft(self.back_t.popleft())
    
    def forward(self):
        if self.forward_t:
            temp = copy.deepcopy(self.recent_t)
            self.back_t.appendleft(temp.popleft())
            self.recent_t.appendleft(self.forward_t.popleft())    

def solution(maxSize, actions):
    p = people()
    for action in actions:
        if action == "B":
            p.back()
        elif action == "F":
            p.forward()
        else:
            p.direct(action)
    result = list(p.recent_t) # 방문목록을 보여줌
    return result[:maxSize]


print(solution(3, ["1", "2", "3", "4", "5"]))
print(solution(1, ["B", "F"]))
print(solution(3, ["1", "3", "2", "B", "4", "F"]))


# 3개를 동시에 실행했을 때
# ['5', '4', '3']
# ['5']
# ['5', '5', '4']
# 이렇게 나오는건 뭔 이유?

# 여기서 문제가 발생하는 원인은 people 클래스의 deque들이 클래스 변수로 선언되어 있기 때문입니다.
# 클래스 변수는 모든 인스턴스에서 공유되는 변수입니다.
# 따라서, people 클래스의 객체가 여러 번 생성될 때(즉, solution 함수가 여러 번 호출될 때),
# 각각의 객체가 동일한 deque를 공유하게 됩니다.
# 이로 인해 예상치 못한 부작용이 발생하여 결과가 일관성이 없게 나오는 것입니다.
# 이를 해결하기 위해 deque를 인스턴스 변수로 바꾸어 각 객체가 자신만의 deque를 가지도록 하는 것이 좋습니다.
