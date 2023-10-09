def solution(s, skip, index):
    skip = set(skip)
    answer = ''
    for i in s:
        now = ord(i)
        
        for j in range(index):
            while True:
                now += 1
                if now == 123:
                    now = 97
                if chr(now) not in skip:
                    break
            
        answer += chr(now)
            
            
    
    return answer