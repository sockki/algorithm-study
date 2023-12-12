def solution(plans):
    answer = []
    for plan in plans:
        a = plan[1].split(":")
        plan[1] = int(a[0])*60 + int(a[1])
        plan[2] = int(plan[2])
    
    plans.sort(key=lambda x: -x[1])
    left = []
    nowtime = 0
    nowing = 0
    nowname = ""
    nowname,nowtime,nowing = plans.pop()
    while plans:
        if nowtime + nowing > plans[-1][1]:
            left.append([nowname, nowing - (plans[-1][1] - nowtime)])
            nowname,nowtime,nowing = plans.pop()
        elif nowtime + nowing == plans[-1][1]:
            answer.append(nowname)
            nowname,nowtime,nowing = plans.pop()
        elif nowtime + nowing < plans[-1][1]:
            if left:
                nowtime += nowing
                answer.append(nowname)
                nowname,nowing = left.pop()
            else:
                answer.append(nowname)
                nowname,nowtime,nowing = plans.pop()
                
    answer.append(nowname)
        
    while left:
        a,b = left.pop()
        answer.append(a)
    return answer