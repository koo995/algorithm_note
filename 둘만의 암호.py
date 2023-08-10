def next_char(s):
    result = ord(s) + 1
    if result > ord("z"):
        result = ord("a")
    return chr(result)
    
def solution(s, skip, index):
    answer = ""
    for j in range(len(s)):
        count = 0
        c = s[j]
        while (count < index) :
            if (skip.find(next_char(c)) == -1): 
                c = next_char(c)
                count += 1
            else:
                c = next_char(c)
        answer += c
    answer 
    return answer