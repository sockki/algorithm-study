from collections import defaultdict

def solution(clothes):
    answer = 0
    result = 1
    dic = defaultdict(list)
    for i in clothes:
        dic[i[1]].append(i[0])
        
    for i in dic:
        result = result * (len(dic[i]) + 1)
    answer += result - 1
  
        
    
    
    return answer