def solution(p):
    answer = slide(p)
    return answer

def slide(p):
    left = 0
    right = 0
    ind = 0
    
    if p == "":
        return ""
    
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if right == left:
            ind = i + 1
            break
    
    first = p[:ind]
    second = p[ind:]
    
    result = search(first)
    
    if result:
        retry = slide(second)
        answer = first + retry
    else:
        retry = slide(second)
        new = ""
        for i in first[1:-1]:
            if i == "(":
                new += ")"
            elif i == ")":
                new += "("
        answer = "(" + retry + ")" + new
    
    return answer

def search(p):
    right = True
    l = 0
    r = 0
    for i in range(len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        
        if r > l:
            right = False
    
    return right

# 문제를 좀 읽자 제발
# str를 for문을 쓸 때는 왠만하면 for i in range(len(p)) 를 쓰자