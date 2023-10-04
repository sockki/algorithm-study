def solution(participant, completion):
    dic = {}
    for i in completion:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in participant:
        if i in dic and dic[i] >= 1:
            dic[i] -= 1
        else:
            return i
    
    return dic