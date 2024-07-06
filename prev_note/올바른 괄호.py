from collections import deque


def solution(s):
    answer = True
    stack = deque()
    for e in s:
        if e == "(":
            stack.append(e)
        else:  # )일때 stack에서 빼낸다. 근데 빼낼 것이 없으면 false?
            if stack:
                stack.pop()
            else:
                answer = False

    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))


def solution2(s):
    stack = []
    for a in s:
        if a == "(":
            stack.append(a)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    else:
        return True
