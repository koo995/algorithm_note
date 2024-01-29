from functools import cmp_to_key


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
    dic = sorted(
        dic.items(), key=lambda item: item[1][0], reverse=True
    )  # 총 시간 기준으로 정렬. 내림차순
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
# print(
#     solution(
#         ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     )
# )


def solution2(genres, plays):
    import heapq
    from functools import cmp_to_key

    def comparator(a, b):
        if a[0] != b[0]:
            return -1 if a[0] < b[0] else 1
        else:  # a와 b가 같다면?
            return 1 if a[1] < b[1] else -1

    dic = {}
    N = len(genres)
    for i in range(N):
        genre, play = genres[i], plays[i]
        if genre not in dic:
            dic[genre] = [
                play,
                [(play, i)],
            ]  # [total, [(play, 0), (play, 1)]] 이런식으로 구성될 것이다.
        else:
            dic[genre][0] += play
            heapq.heappush(dic[genre][1], (play, i))
    dic_items = list(dic.items())
    dic_items.sort(key=lambda lst: lst[1][0], reverse=True)
    print("dic_items: ", dic_items)
    result = []
    for g, l in dic_items:
        total, items = l
        # items는 [(150, 2), (500, 0), (800, 3)] 이렇게 생겼다. heapq을 이용해서 기본적으로 작은녀석이 왼쪽에 있는데... 동일한 경우... 작은녀석도 왼쪽에 있다 하지만 원하는건 큰 녀석이 아니라 작은녀석
        # 하... 여기서 새롭게 정렬을 할꺼면 heapq을 쓸 이유가 없는데... 문제를 처음부터 똑바로 읽을걸 그랫나?
        items.sort(key=cmp_to_key(comparator))
        count = 0
        for item in items[::-1]:
            if count == 2:
                break
            result.append(item[1])
            count += 1
    return result


# dic:  {'classic': [[150, 2], [650, -1], [500, 0]], 'pop': [[600, 1], [600, -1]]} 이게 왜 이런 결과가 나온것일까?
print(
    solution2(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)

# heapq로 다루는 객체를 인덱스를 이용하여 임의로 조작하니까 뜻하지 않는 문제가 계속 발생했다
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다. 이 조건을 판단하지 않았다.
# 뭐 불필요하게 heapq을 쓰긴했지만... cmp_to_key을 사용해볼 좋은 기회였다
