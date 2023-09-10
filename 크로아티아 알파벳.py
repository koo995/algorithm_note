cro_alphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
input_str = list(input()) # 100개 또는 그 이상? ljes=njak
count = 0
s = 0
e = 0
while( s <= e and s<len(input_str)):
    if input_str[s] in ["c", "d", "l", "n", "s", "z"]:
        if "".join(input_str[s:e+2]) in cro_alphas:
            count += 1
            s = e + 2
            e = s
            continue
        elif "".join(input_str[s:e+3]) == "dz=":
            count += 1
            s = e + 3
            e = s
            continue
        else:
            s += 1
            e = s
            count += 1
            continue
    s += 1
    e = s
    count += 1
print(count)