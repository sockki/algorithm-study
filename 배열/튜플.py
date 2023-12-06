def solution(s):
    answer = []
    s = s.replace("{","").replace("},"," ").replace("}","").split(" ")
    for i,v in enumerate(s):
        s[i] = v.split(",")
    s.sort(key=lambda x:len(x))
    dic = {}
    for i in s:
        for j in i:
            if j in dic:
                continue
            else:
                dic[j] = 1
                answer.append(int(j))
    return answer