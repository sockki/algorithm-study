def solution(X, Y):
    answer = ''
    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    
    for i in X:
        numx[i] += 1
        
    for i in Y:
        numy[i] += 1
        
    for i in range(9,-1,-1):
        k = str(i)
        nownum = min(numx[k],numy[k])
        
        if answer == '' and k == "0" and nownum != 0:
            return "0"
        answer  = ''.join([answer, nownum*k])
        
    if answer == '':
        return "-1"
    
        
    return answer

#정렬을 빠르게 하는 방법에 대한 생각
#answer  = ''.join([answer, nownum*k])