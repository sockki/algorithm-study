def solution(board, moves):
    ba = []
    gile = len(board)
    anoboard = [[] for _ in range(gile)]
    for i in board:
        index = 0
        for j in i:
            if j:
                anoboard[index].append(j)
            index += 1

    answer = 0
    for i in moves:
        if not anoboard[i-1]:
            continue
        ba.append(anoboard[i-1].pop(0))

        if len(ba) >= 2:
            if ba[-1] == ba[-2]:
                ba.pop()
                ba.pop()
                answer += 2

    return answer

# 단순하게 숫자가 나올 떄 까지 if문을 돌려도 속도가 되는 듯 하다.
# cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
# 첫 for 문을 한 줄로 줄인 것이 이것 인듯 하다.
