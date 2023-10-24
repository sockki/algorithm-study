from collections import defaultdict

def solution(before, after):
    answer = 0
    dic = defaultdict(int)
    for i in before:
        dic[i] += 1
    for i in after:
        if dic[i] and dic[i] > 0:
            dic[i] -= 1
        else:
            return 0
        
    return 1