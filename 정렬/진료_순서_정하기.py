def solution(emergency):
    answer = []
    emer_avg = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(emer_avg.index(i)+1)
    return answer