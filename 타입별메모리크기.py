import sys
from enum import Enum
input = sys.stdin.readline
array = list(input().split())

MAX_MEMORY_TABLE_SIZE = 128
MAX_UNIT_MEMORY_SIZE = 8
MEMORY_TABLE = [[] for _ in range(16)]
UNIT_MEMORY = []

class Type(Enum):
    BOOL = (1, "#")
    SHORT = (2, "##")
    FLOAT = (4, "####")
    INT = (8, "########")
    LONG = (16, "################")

    def __init__(self, size, hash):
        self.size = size
        self.hash = hash
    
    @property
    def type_list():
        return [member for _, member in Type.__members__.items()]


def allocate_memory(type):
    global MEMORY_TABLE
    for unit_memory in MEMORY_TABLE:
        if len(unit_memory) > UNIT_MEMORY_SIZE:
            continue

def check_unit_memory():
    global UNIT_MEMORY
    sum = 0
    for type in UNIT_MEMORY:
        sum += type.size
    return sum

def to_icon(unit_mem: list):
    str = ""
    for t in unit_mem:
        str += t.hash
        if t.name != "BOOL":
            str += "."
        
    str += type.hash
    return 0
    

def allocate_unit_memory(type: Type):
    global UNIT_MEMORY

    UNIT_MEMORY.append(type)
    result = check_unit_memory() # 유닛 메모리에 현재 차있는 정도
    if result > MAX_UNIT_MEMORY_SIZE:
        temp = UNIT_MEMORY.pop() # 타입 하나더 추가했는데 크기가 8을 초과한다면 마지막에 넣은것을 빼버린다. 그후 남은 녀석들로 처리. 뺀 녀석은 따로 보관
        str = to_icon(UNIT_MEMORY) # 샵으로 구성된 문자열을 받는다
        # 마지막에 뺏던것을 다음메모리로 새롭게 넣어준다.
        UNIT_MEMORY.clear()
        UNIT_MEMORY.append(temp)
        allocate_memory(str) # 하나의 메모리에 해당하는 만큼 채워준다.
        
    
    

def function(array):
    for type in array:
        # 일치하는 타입을 찾아 유닛메모리에 할당
        for member in Type.type_list:
            if type == member.name:
                allocate_unit_memory(member)
        if unit_memory > MAX_UNIT_MEMORY_SIZE:
                


# 우선 들어온 type을 체크하여 8바이트까지의 기준을 정해야 한다.
# 어디까지 단위 메모리에 담을지 기준을 정해야하지 않을까?
# 하나하나 차근차근 가보자구...