def solution(babbling):
    answer = 0
    babbs = {"aya","ye","woo","ma"}
    for bab in babbling:
        now = ""
        past = ""
        arr = list(bab)
        while arr:
            now += arr.pop(0)
            if now in babbs:
                if now == past:
                    break
                past = now
                now = ""
        if now == "":
            answer += 1
    return answer