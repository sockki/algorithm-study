def solution(s):
    answer = 0
    result = set()
    length = len(s)
    for i in range(length):
        if i == length - 1:
            result.add(1)
            break
        past = i - 1
        nxt = i + 1
        now = 1
        while True and i != 0:
            if s[past] == s[nxt]:
                now += 2
            else:
                result.add(now)
                break
    
            if past == 0 or nxt == length-1 :
                result.add(now)
                break
            else:
                past -= 1
                nxt += 1
                
        past = i
        nxt = i+1
        now = 0
        while True:
            if s[past] == s[nxt]:
                now += 2
            else:
                result.add(now)
                break
                
            if past == 0 or nxt == length-1 :
                result.add(now)
                break
            else:
                past -= 1
                nxt += 1
    

    return max(result)