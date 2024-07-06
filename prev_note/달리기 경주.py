def solution(players, callings):
    p_idx = {p:i for i, p in enumerate(players)} # 딕셔너리를 파이썬 스럽게 쓰는 방법은 이런 것도 잇구나
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4} 이러한 구조를 가진다.
    for call in callings: # 어쨋든 이름을 부르면 변경을 해줘야 하는것 같은데...
        call_p_idx = p_idx[call]
        pre_p = players[call_p_idx-1]
        # players 도 업데이트 해주고 p_idx 도 업데이트 해줘야 한다.
        players[call_p_idx-1], players[call_p_idx] = call, pre_p
        p_idx[call], p_idx[pre_p] = call_p_idx - 1, call_p_idx
    return players