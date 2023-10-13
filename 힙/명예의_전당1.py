def solution(k, score):
    answer = []
    honor = []
    for i, nowsco in enumerate(score):
        if i < k:
            honor.append(nowsco)
            answer.append(min(honor))
        else:
            if nowsco > answer[-1]:
                honor.append(nowsco)
                honor.sort()
                honor = honor[1:]
                answer.append(honor[0])
            else:
                answer.append(answer[-1])
    return answer