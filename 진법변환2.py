from string import ascii_uppercase
N, B = map(int, input().split())
# 10진법 N을 B진법으로...
result = ""
letters = {}
for idx, e in enumerate(list(ascii_uppercase)):
    letters[idx+10] = e

while(True):
    if N < B:            
        if N >= 10:
            N = letters[N]
        result = str(N) + result
        break
    if (N % B) >= 10:
        s = letters[N%B]
        result = s + result
    else:
        result = str((N % B)) + result
    N = N // B
print(result)

#
N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])