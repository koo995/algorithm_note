def solution(array):
    type_size = {"bool": 1, "short": 2, "float": 4, "int": 8, "long": 16} 
    result = ''
    current_block = 0 # 이 녀석이 인덱스 역할을 해줄거야.
    block_table = [[""] for _ in range(16)]
    
    for type in array:
        if type_size[type] < 8:
            if len(block_table[current_block][0]) >= 8 : # 여기서 나머지가 0인 경우로 하니까 제일 처음 0인 경우도 0이니까 index 1부터 채워지네... 
                # 하나의 메모리가 가득 찼다면, 다음 메모리에 넣어야 겠지?
                current_block += 1 
                # 가득찬 후 새로운 block에 넣을때는 앞에서 부터 넣으니까 패딩이 필요없겠군
                block_table[current_block][0] += "#" * type_size[type]
            else : # 우선 하나의 단위 메모리가 가득 차지 않았다면 이후 추가해 준다. 패딩을 고려해야 한다.
                if type == "bool":
                    block_table[current_block][0] += "#"
                if type == "short":
                    # short을 넣었을때 8을 넘는 경우가 있을 수 있지 그것을 먼저 고려하자
                    if len(block_table[current_block][0]) + type_size[type] > 8:
                        current_block += 1
                    # 만약에 2배수가 아니라면 패딩을 넣어야 겠지? 얼만큼? 그냥 하나만 넣으면 어떤 상황이건 되지 않나?
                    if len(block_table[current_block][0]) % 2 != 0:
                        block_table[current_block][0] += "."
                    block_table[current_block][0] += "#" * type_size[type]
                if type == "float":
                    if len(block_table[current_block][0]) + type_size[type] > 8:
                        current_block += 1
                    # 만약에 4배수가 아니라면 패딩을 추가해 줘야지
                    if len(block_table[current_block][0]) % 4 != 0:
                        padding = 4 - len(block_table[current_block][0]) % 4
                        block_table[current_block][0] += "." * padding
                    block_table[current_block][0] += "#" * type_size[type]
                
        else: # type의 크기가 8또는 16인 경우야.
            # 블락이 가득찼다면 그냥 8개씩 hash을 채워준다.
            if len(block_table[current_block][0]) >= 8:
                current_block += 1
                block_table[current_block][0] += "#" * 8
                # long타입이라면 한번더 채워줘야 되지
                if type == "long":
                    current_block += 1
                    block_table[current_block][0] += "#" * 8
            # block이 가득차지 않았다면, 먼저 넣어줘야 하는데... 넣었을 경우 사이즈 초과가 발생해 그러면 패딩을 고려하여 block을 채우고 다음 블락에 넣어줘야 겠군
            else:
                if len(block_table[current_block][0]) + type_size[type] > 8: # 넣었을때 사이즈가 초과한다면
                    # 그렇다면 패딩은 얼만큼? 8- 나머지만큼
                    padding = 8 - len(block_table[current_block][0]) % 8
                    block_table[current_block][0] += "." * padding
                    # 패딩을 다 채워주었다면 위랑 같네
                    current_block += 1
                    block_table[current_block][0] += "#" * 8
                    # long타입이라면 한번더 채워줘야 되지
                    if type == "long":
                        current_block += 1
                        block_table[current_block][0] += "#" * 8
                else: # 초과가 발생하지 않는 다는 것은 처음인 경우겟군
                    block_table[current_block][0] += "#" * 8

                    
    return block_table
    # count = 0
    # for block in block_table:
    #     count += 1
    #     if count > 16:
    #         return "HALT"
    #     result += block[0] # block의 모양은 ["###....."] 이런 모양이니까 index 0추가
    #     result

result = solution(["bool", "float", "int", "bool", "short", "float", "bool", "bool", "long"])
print(result)

# 괜히 enum이나 이런거 쓸려해서 어렵게 가는 것이였나...
# 이런 문제는 딕셔너리를 쓰는게 유용해 보이네... 사실 평상시에 딕셔너리를 잘 안써봐서 덜 익숙한듯...

# table 안에 모양이 완전 이상하게 들어가 있네... ['#', '#', '#', '#', '#', '#', '#', '#']이런 모양이라니...
# 처음부터 string에다 str += "#" *5 하면 "#####"이 될텐데
# 하나의 list인 []안에다가 "#" * 5를 하니까 ["#", ...."] 이렇게 되는구나
# 그렇다면 내가 원하는 ["#####"] 이렇게 저장될려면 어케하지?
# 방법은... index0을 사용하여 미리 정의한 str을 뽑아오기, 또 다른 변수를 만들어서 8개가 되면 추가하기?
# 아니면 list에 있는 모든 요소를 합하는? join이 있긴한데... 시간제한 때문에 써도 될지 모르겟다

# 또 왜 처음 index는 아무것도 안채워지지? 나머지가 0인 경우로 처리해서 그렇구나 0을 무언가로 나눌때 나머지가 0이니
# 그렇다면 사이즈가 큰 경우로 하면? 처음이 모조리 padding으로 채워지네 ㅅㅂ 이런 경우는 뭘로 해야하지
# 넣었을떼 초과하냐 안하냐로 처리했음. 사실 되게 기본적으로 따질 문제인가
# 근데 너무 if 와 else가 난잡한데... 함수들로 분리하는게 나았을려나...