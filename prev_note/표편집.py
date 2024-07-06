# cmds가 최대 20만이고 제거 또는 복구에도 n의 갯수만큼 걸리는데... 최대 운이 없으면 20만 곱하기 100만이 된다.
# 그러면 나는 최대한 리스트의 크기를 바꾸지 않는 방향이나 제거 또는 insert가 쉬운 방향으로 가야한다.
# 우선 스택이나 큐가 있다.


def solution(n, k, cmds):
    from collections import deque

    def operate(q: deque, stack: list, cmd):
        if cmd[0] == "D":
            q.rotate(
                -int(cmd[-1])
            )  # 음... 이것도 안에든 숫자가 크다면 그만큼 잡아먹긴 하는데
            return
        elif cmd[0] == "U":
            q.rotate(int(cmd[-1]))
            return
        elif (
                cmd[0] == "C"
        ):  # 삭제하는 경우니까... 첫재녀석 삭제하는 경우, 가운데, 마지막 삭제하는 경우를 정해보자.
            if (
                    q[0] > q[1]
            ):  # 여기서 가장 마지막인 녀석을 비교해야 하는데.. 딱 하나 남아서 그것마저 제거할 상황은 주어지지 않는다.
                del_node = q.popleft()
                prev_node = q[-1]  # 이 녀석이 사실상 나보다 위에 있는 녀석이다.
                stack.append((del_node, prev_node))
                q.rotate(1)
                return
            del_node = (
                q.popleft()
            )  # 여기서 다 삭제하는 경우는 남지가 않는데... 대신 하나만 남을 수 있다.
            prev_node = q[-1]
            stack.append((del_node, prev_node))  # 내가 삭제된 녀석
            return
        elif cmd[0] == "Z":
            del_node, prev_node = stack.pop()

            prev_index = q.index(
                prev_node
            )  # 여기서 시간을 꽤 잡아먹을까?... 이것을 위해서 q에서 현재 인덱스를 다 저장한다면 이동할때마다 수정해줘야하는 번거로움이 있다... 이건 아웃
            q.insert(
                (prev_index + 1) % len(q), del_node
            )  # 이것도 꽤 시간을 잡아먹을텐데?
            return

    q = deque([i for i in range(n)])  # 제일 앞에 있는 녀석이 현 위치.
    stack = []
    q.rotate(-k)
    print("시작전 q상태: ", q)
    for cmd in cmds:
        operate(q, stack, cmd)
        print("cmd: ", cmd)
        print("stack: ", stack)
    print("종료된 q: ", q)
    answer = ""
    for node in range(n):
        if node in q:
            answer += "O"
            continue
        answer += "X"
    return answer


# 시간초과가 어디서 발생하는 것일까? 아니 애초에 실패하는 지점이 있는데 그 부분이 틀렸단 것이잖아. 문제를 똑바로 안읽었나봐
# 일단 그 실패지점의 이유를 찾자. 모든 것이 다 삭제된 경우라면...? 그리고 복구해야 하는 상황이면? 문제를 보면 모든것이 다 삭제된 경우는 주어지지 않는다.


def solution1(n, k, cmds):
    from collections import deque

    # 문제는 역시 여기서 발생했다는 것이지?
    def operate(q: deque, stack: list, cmd):
        if cmd[0] == "D":
            pos, move = cmd.split(" ")
            q.rotate(-int(move))
        elif cmd[0] == "U":
            pos, move = cmd.split(" ")
            q.rotate(-int(move))
        elif cmd[0] == "C":
            if (
                    q[0] > q[1]
            ):  # 이 조건이면 마지막 행인 것을 충족하는 가? 행은 항상 위에서 아래로 커질꺼야
                del_node = q.popleft()
                prev_node = q[-1]
                stack.append((del_node, prev_node))
                q.rotate(1)  # 자동으로 업과 같은 작동을 해줘야지?
                return
            del_node = q.popleft()  # 자동으로 다운이 나타날 것이다.
            prev_node = q[-1]  # 이 녀석은 나보다 위에 있는 녀석이다.
            stack.append((del_node, prev_node))
        elif cmd[0] == "Z":
            del_node, prev_node = stack.pop()  # 삭제된 녀석과 그 녀석 앞에 있던 것이다.
            prev_index = q.index(prev_node)
            # 먼저 가장 앞으로 복귀되야 하는 상황을 보자. 아니 그런 일은 없어. 선택된 녀석이 바뀌지는 않으니까
            # prev_index가 현재 가장 뒤에 있다면 앞으로. 넣은 다음 따로 처리할 것은 없는가? 아 선택된 녀석이 바뀌면 안되지.
            # 복구하는것은 그러면 어떤 상황이든 prev_idx뒤에가 맞는거 같은데...
            q.insert(prev_index + 1, del_node)

    q = deque([i for i in range(n)])
    stack = []
    q.rotate(-k)
    for cmd in cmds:
        operate(q, stack, cmd)
    answer = ""
    for node in range(n):
        if node in q:
            answer += "O"
            continue
        answer += "X"
    return answer


# 이건 다른 녀석의 풀이다.
def solution2(n, k, cmds):
    class Node:
        def __init__(self, prev=None, next=None):
            self.del_state = False
            self.prev = prev
            self.next = next

        def is_deleted(self):
            return self.del_state

        def __str__(self):
            return f"del_state: {self.del_state} prev: {self.prev} next: {self.next}"

        def __repr__(self):
            return self.__str__()

    def operate(
            cmd, table, point, stack
    ):  # point는 지역변수로써 주소값을 참고하지 않고 있다.
        if cmd[0] == "D":
            # point가 아래로 내려가야 한다.
            for _ in range(int(cmd[-1])):
                cur_node = table[point]
                point = cur_node.next
            return point
        elif cmd[0] == "U":
            for _ in range(int(cmd[-1])):
                cur_node = table[point]
                point = cur_node.prev
            return point
        elif cmd[0] == "C":  # 이 경우에 연결리스트의 관계를 바꿔야 한다.
            stack.append(point)
            table[point].del_state = True

            l, r = table[point].prev, table[point].next

            if l or l == 0:
                table[l].next = r
            # 마지막행이면
            if r:
                table[r].prev = l
                point = r
            else:
                point = l
            return point
        else:  # 자 이제 복구는 어케 할거냐
            del_node_idx = stack.pop()
            table[del_node_idx].remove = False

            prev, next = table[del_node_idx].prev, table[del_node_idx].next
            # 복원된 행이 첫째행이아니라면
            if prev:
                table[prev].next = del_node_idx
            if next:
                table[next].prev = del_node_idx
            return point

    table = [Node(i - 1, i + 1) for i in range(n)]  # 이 모든 것들은 dic으로 관리한다.
    table[0].prev = n - 1
    table[-1].next = 0
    stack = []
    point = k
    for cmd in cmds:
        point = operate(cmd, table, point, stack)

    answer = ""
    for i in range(n):
        if table[i].del_state:
            answer += "X"
        else:
            answer += "O"

    return answer


def solution3(n, point, cmds):
    class Node:
        def __init__(self, prev=None, next=None):
            self.del_state = False
            self.prev = prev
            self.next = next

    def operate(
            cmd, table, point, stack
    ):  # point는 지역변수로써 주소값을 참고하지 않고 있다.
        if cmd[0] == "D":
            # point가 아래로 내려가야 한다.
            for _ in range(int(cmd[-1])):
                cur_node = table[point]
                point = cur_node.next
            return point
        elif cmd[0] == "U":
            for _ in range(int(cmd[-1])):
                cur_node = table[point]
                point = cur_node.prev
            return point
        elif cmd[0] == "C":  # 이 경우에 연결리스트의 관계를 바꿔야 한다.
            stack.append(point)
            table[point].del_state = True

            l, r = table[point].prev, table[point].next

            if l or l == 0:
                table[l].next = r
            # 마지막행이면
            if r:
                table[r].prev = l
                point = r
            else:
                point = l
            return point
        else:  # 자 이제 복구는 어케 할거냐
            del_node_idx = stack.pop()
            table[del_node_idx].del_state = False

            prev, next = table[del_node_idx].prev, table[del_node_idx].next
            # 복원된 행이 첫째행이아니라면
            if prev:
                table[prev].next = del_node_idx
            if next:
                table[next].prev = del_node_idx
            return point

    table = [Node(i - 1, i + 1) for i in range(n)]
    table[0].prev = None
    table[-1].next = None
    stack = []
    for cmd in cmds:
        point = operate(cmd, table, point, stack)

    answer = ""
    for i in range(n):
        if table[i].del_state:
            answer += "X"
        else:
            answer += "O"

    return answer


def solution4(n, point, cmds):
    class Node:
        def __init__(self, prev=None, next=None):
            self.del_state = False
            self.prev = prev
            self.next = next

    table = [Node(i - 1, i + 1) for i in range(n)]
    table[0].prev = None
    table[-1].next = None
    stack = []
    for cmd in cmds:
        if cmd[0] == "U":
            pos, move = cmd.split()
            for _ in range(int(move)):
                point = table[point].prev
        elif cmd[0] == "D":
            pos, move = cmd.split()
            for _ in range(int(move)):
                point = table[point].next

        # 지금 다른 무엇도 아닌 이 부분에서 오류가 발생했다. 하 시발
        # 나중에 실행할때는 아래거 지우자... 내가 ㅅㅂ 레벨 3을 이렇게 까지 못풀리가 없잔하.....
        if cmd[0] == "D":
            # point가 아래로 내려가야 한다.
            for _ in range(int(cmd[-1])):
                point = table[point].next
        elif cmd[0] == "U":
            for _ in range(int(cmd[-1])):
                point = table[point].prev

        elif cmd[0] == "C":  # 이 경우에 연결리스트의 관계를 바꿔야 한다.
            stack.append(point)
            table[point].del_state = True
            l, r = table[point].prev, table[point].next
            if l or l == 0:
                table[l].next = r
            # 마지막행이면
            if r:
                table[r].prev = l
                point = r
            else:
                point = l
        else:  # 자 이제 복구는 어케 할거냐
            del_node_idx = stack.pop()
            table[del_node_idx].del_state = False

            prev, next = table[del_node_idx].prev, table[del_node_idx].next
            # 복원된 행이 첫째행이아니라면
            if prev:
                table[prev].next = del_node_idx
            if next:
                table[next].prev = del_node_idx

    answer = ""
    for i in range(n):
        if table[i].del_state:
            answer += "X"
        else:
            answer += "O"

    return answer


# 시간초과가 어디서 발생하는 것일까? 아니 애초에 실패하는 지점이 있는데 그 부분이 틀렸단 것이잖아. 문제를 똑바로 안읽었나봐
# 일단 그 실패지점의 이유를 찾자. 모든 것이 다 삭제된 경우라면...? 그리고 복구해야 하는 상황이면?
# class 로 만들어서 했는데... 또 테케에서 틀린다. 내가 분명 병신짓 하나 한거 같은데 도대체 뭐지
# 하 병신인가... 완전히 문제를 잘못 이해했네... 위로 계속 올라가면 아래로 가는거 아니잖아
# print(
#     solution2(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
# )


def solution5(n, current_point, cmds):
    class Node:
        def __init__(self, prev_idx, next_idx, is_deleted=False):
            self.prev = prev_idx
            self.next = next_idx
            self.is_deleted = is_deleted

        def __repr__(self):
            return f"Node(prev = {self.prev}, next = {self.next}, is_deleted = {self.is_deleted})"

    def print_answer(t):
        answer = ""
        for node in t:
            if node.is_deleted:
                answer += "X"
            else:
                answer += "O"
        print("answer: ", answer)

    recent_deleted = []
    table = [Node(i-1, i+1) for i in range(n)]
    table[0].prev = None
    table[-1].next = None
    print("table: ", table)

    for cmd in cmds:
        print("current point: ", current_point)
        if cmd[0] == "D":
            _, n = cmd.split()
            for _ in range(int(n)):
                current_point = table[current_point].next
        if cmd[0] == "U":
            _, n = cmd.split()
            for _ in range(int(n)):
                current_point = table[current_point].prev
        if cmd[0] == "C":
            table[current_point].is_deleted = True
            recent_deleted.append(current_point)
            if table[current_point].prev is not None:
                table[table[current_point].prev].next = table[current_point].next
            if table[current_point].next is not None:
                table[table[current_point].next].prev = table[current_point].prev
            current_point = table[current_point].next if table[current_point].next is not None else table[current_point].prev
        if cmd[0] == "Z":
            idx = recent_deleted.pop()
            table[idx].is_deleted = False
            prev, next = table[idx].prev, table[idx].next
            if prev is not None:
                table[prev].next = idx
            if next is not None:
                table[next].prev = idx

    answer = ""
    for node in table:
        if node.is_deleted:
            answer += "X"
        else:
            answer += "O"
    print("answer: ", answer)

solution5(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])