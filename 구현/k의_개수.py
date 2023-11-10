def solution(i, j, k):
    answer = 0
    k = str(k)
    for a in range(i, j+1):
        b = str(a)
        answer += b.count(k)
        
    return answer