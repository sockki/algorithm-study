from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    dic = defaultdict(set)
    dic2 = defaultdict(int)
    for i in id_list:
        dic[i]
        dic2[i]
        
    for i in report:
        j = i.split(" ")
        dic[j[1]].add(j[0])
        
    for i in dic:
        if len(dic[i]) >= k:
            for j in dic[i]:
                dic2[j] += 1
                
    for i in dic2.values():
        answer.append(i)
    
    return answer