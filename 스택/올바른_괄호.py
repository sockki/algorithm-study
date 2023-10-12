def solution(s):
    now = 0
    for i in s:
        if i == "(":
            now += 1
        elif i == ")":
            now -= 1
            if now < 0:
                return False
    if now == 0:
        return True
    else:
        return False
