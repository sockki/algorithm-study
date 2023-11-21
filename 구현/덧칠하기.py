def solution(n, m, section):
    answer = 0
    last = 0
    for i in section:
        if i > last:
            answer += 1
            last = i + m - 1
    return answer