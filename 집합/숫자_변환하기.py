def solution(x, y, n):
    nowset = set()
    nextset = set()
    nowset.add(x)
    index = 0
    
    while nowset:
        if y in nowset:
            return index
        index += 1
        for now in nowset:
            if now + n <= y:
                nextset.add(now + n)
            if now * 2 <= y:
                nextset.add(now * 2)
            if now * 3 <= y:
                nextset.add(now * 3)
        
        nowset = nextset
        nextset = set()
    
    return -1