def solution():
    n = int(input())
    members = [(input().split(), i) for i in range(n)]
    members.sort(key=lambda member:(int(member[0][0]), member[1]))
    for member in members:
        print(" ".join(member[0]))

solution()