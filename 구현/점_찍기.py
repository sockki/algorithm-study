def solution(k, d):
    answer = 0
    d_2 = d**2
    x = 0
    while x <= d:
        max_v = (d_2 - x**2)**(0.5)
        rest = max_v % k
        answer += (max_v - rest) // k + 1
        x += k
                
    return answer

# 원 문제가 나오면 원의 방정식을 사용해서 풀어보자