from collections import defaultdict


def solution(genres, plays):
    summary = defaultdict(list)
    plays_summary = defaultdict(int)
    for index, (genre, play) in enumerate(zip(genres, plays)):
        summary[genre].append([index, play])
        plays_summary[genre] += play

    by_plays = sorted(plays_summary.items(), key=lambda x: -x[1])
    result = []

    for genre, _ in by_plays:
        songs = sorted(summary[genre], key=lambda x: -x[1])[:2]
        result.extend([song for song, _ in songs])

    return result

# from collections import defaultdict
# defaultdict은 키가 존재하지않으면 0의 value 값을 리턴한다.

# for index, i in enumerate(list)
# index에 인덱스 값을, i에 list의 요소를 리턴해준다.

# list.extend
# append는 그 파라미터 값 그대로를 넣는다. extend는 그 안의 정수나,string 값만 넣는다.
