from collections import defaultdict

def solution(topping):
    answer = 0
    dic = defaultdict(int)
    b = set([])
    for i in topping:
        dic[i] += 1
    
    for i in topping:
        dic[i] -= 1
        b.add(i)
        if not dic[i]:
            dic.pop(i)
        if len(dic) == len(b):
            answer += 1
        
            
    return answer