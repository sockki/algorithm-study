def solution(s):
    answer = 0
    firststr = ""
    firstnum = 0
    notfirstnum = 0
    
    for i in s:
        if not firststr:
            firststr = i
            firstnum += 1
        else:
            if firststr == i:
                firstnum += 1
            else:
                notfirstnum += 1
                if notfirstnum == firstnum:
                    answer += 1
                    firststr = ""
        
    if firststr:
        answer += 1
                    
                
    
    
        
    return answer