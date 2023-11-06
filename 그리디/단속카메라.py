def solution(routes):
    answer = 0
    routes = sorted(routes)
    before = [-30000, -30000]
    for now in routes:
        if now[0] <= before[1]:
            before = [now[0], min(before[1], now[1])]
        else:
            answer += 1
            before = now
    return answer

# 그리디는 제일 작은 것 부터 또는 제일 큰 것 부터 