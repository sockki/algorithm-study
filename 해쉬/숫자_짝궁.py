from collections import defaultdict

def solution(X, Y):
    arr = []
    answer = ''
    dic = defaultdict(int)
    for i in X:
        dic[int(i)] += 1
        
    for i in Y:
        j = int(i)
        if dic[j] and dic[j] > 0:
            dic[j] -= 1
            arr.append(j)
    
    arr.sort(reverse=True)
    if not arr:
        return "-1"
    if len(set(arr)) == 1 and 0 in arr:
        return "0"
    
    for i in arr:
        answer += str(i)
    return answer