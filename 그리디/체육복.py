from collections import defaultdict

def solution(n, lost, reserve):
    answer = 0
    dic = defaultdict(int)

    for i in range(1, n + 1):
        dic[i] += 1
    for i in lost:
        dic[i] -= 1
    for i in reserve:
        dic[i] += 1
    
    for i in range(1,n+1):
        if dic[i] > 1 and i > 1 and dic[i-1] == 0:
            dic[i-1] += 1
            dic[i] -= 1
        elif dic[i] > 1 and dic[i+1] == 0:
            dic[i+1] += 1
            dic[i] -= 1
                
    for i in range(1,n+1):
        if dic[i] >= 1:
            answer += 1
        
    return answer