from functools import cmp_to_key


# def lst_compare(a, b):
#     # [[800, 3], [500, 0], [150, 2]] 이렇게 들어온다 했을때
#     if a[0] > b[0]:
#         return -1
#     elif a[0] == b[0]:
#         if a[1] < b[1]:
#             return -1
#         elif a[1] == b[1]:
#             return 0
#         else:
#             return 1
#     else:
#         return 1


def solution(genres, plays):
    dic = {}
    answer = []
    for music in enumerate(zip(genres, plays)):
        music_id = music[0]
        music_genre = music[1][0]
        music_plays = music[1][1]
        if not music_genre in dic:
            dic[music_genre] = [music_plays]
            dic[music_genre].append([music_plays, music_id])
            continue
        dic[music_genre][0] += music_plays  # 총 플레이 시간을 계속 더해준다.
        dic[music_genre].append([music_plays, music_id])
    print("dic: ", dic)
    print("dict_items: ", dic.items())
    dic = sorted(
        dic.items(), key=lambda item: item[1][0], reverse=True
    )  # 총 시간 기준으로 정렬. 내림차순
    print("sorted_dic: ", dic)
    for genre_info in dic:
        musics_sorted_by_plays = sorted(
            (genre_info[1][1:]), key=lambda x: (x[0], -x[1]), reverse=True
        )
        for music in musics_sorted_by_plays[:2]:
            answer.append(music[1])

    return answer


# lst:  [(0, ('classic', 500)), (1, ('pop', 600)), (2, ('classic', 150)), (3, ('classic', 800)), (4, ('pop', 2500))]
# 하나의 뮤직은 (0, ('classic', 500)) 이런 모양.
# 굳이 해시를 써야 하나... 그냥 우선순위큐로 정렬하면 될 듯 한데...
# dict도 정렬이 가능하구나... 아니 단지 items()을 통해 튜플로 만든 후 정렬 하는 거야.
# 자 이젠 재생횟수가 같다면 id를 기준으로 넣어보자.
# 다중조건으로 정렬도 가능하구나. 참고하자. 하나는 오름차순 하나는 내림차순으로 정렬할려면 마이너스를 붙이는 것도 중요해
# 근데 도대체 뭐가 틀린거야... 아아... id값도 내림차순이군....
# enumerate을 사용할때 참고하자... start라는 조건을 줄 수 있고, 값이 3개라면 1개에 다 받을 수 있고. 1에 하나 2에 리스트로 2개를 받을수도 있구나
# 분명히 뭔가 잘못 되었는데... 하.. 미친놈 dic.items() 이렇게 하면 key와 value가 쌍을 이뤄서 튜플로 나오는거지... sort가 대단해서 알아서 정렬해주는게 아니고...
# print(
#     solution(
#         ["classic", "pop", "classic", "classic", "pop", "classic"],
#         [500, 600, 150, 800, 2500, 500],
#     )
# )
print(
    solution(
        ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    )
)
