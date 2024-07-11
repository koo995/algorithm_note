def solution():
    cro_alphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    input_str = list(input())  # 100개 또는 그 이상? ljes=njak
    count = 0
    s = 0
    e = 0
    while s <= e and s < len(input_str):
        if input_str[s] in ["c", "d", "l", "n", "s", "z"]:
            if "".join(input_str[s : e + 2]) in cro_alphas:
                count += 1
                s = e + 2
                e = s
                continue
            elif "".join(input_str[s : e + 3]) == "dz=":
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


def solution2():
    from string import ascii_lowercase

    croa_dic = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    s = input()  # 이 녀석은 최대 100 글자이다
    for ch in croa_dic:
        s = s.replace(ch, "*")
    print("s: ", s)

def solution3():
    cro_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    word = input()
    for alpha in cro_alpha:
        word = word.replace(alpha, "*")
    print(word)


    pass


solution3()
