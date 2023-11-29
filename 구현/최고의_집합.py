def solution(n, s):
    answer = []
    if s // n < 1:
        return [-1]
    num = s // n
    div = s % n
    for i in range(n - div):
        answer.append(num )
    for i in range(n-div, n):
        answer.append(num + 1)
    return answer