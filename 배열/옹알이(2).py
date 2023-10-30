def solution(babbling):
    answer = 0
    dic = {"aya":1, "ye":1, "woo":1, "ma":1}
    
    for bab in babbling:
        now = ""
        before = ""
        for i in bab:
            now += i
            if now in dic:
                if now == before:
                    break
                else:
                    before = now
                    now = ""
        if now == "":
            answer += 1
        
    return answer