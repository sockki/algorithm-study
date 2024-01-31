def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    oneresult = 0
    two = [2,1,2,3,2,4,2,5]
    tworesult = 0
    three = [3,3,1,1,2,2,4,4,5,5]
    threeresult = 0
    index = 0
    for a in answers:
        if a == one[int(index%5)]:
            oneresult += 1
        if a == two[int(index%8)]:
            tworesult += 1
        if a == three[int(index%10)]:
            threeresult += 1
        index += 1
            
    maxcount = max([oneresult,tworesult,threeresult])
    
    if oneresult == maxcount:
        answer.append(1)
    if tworesult == maxcount:
        answer.append(2)
    if threeresult == maxcount:
        answer.append(3)
        
    return answer