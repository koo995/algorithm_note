#왕실의 나이트

cul = input() # loc[0]은 a,b,c loc[1]은 1 2 3
col = ord(cul[0]) - ord('a') +1
row = int(cul[1]) 
loc = [col, row]
print(loc)
count = 0

moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[2,-1],[-2,1],[-2,-1]]
for move in moves:
    next_col = loc[0] + move[0] 
    next_row = loc[1] + move[1]
    if (next_col >= 1 and next_col <= 8 and next_row >= 1 and next_row <= 8):
        count +=1

print(count)