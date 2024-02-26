# A 65
# Z 90
# a 97
# z 122

def solution(s, n):
    s = list(s)
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        else:
            s = ord(i)
            k = s
            for _ in range(n):
                print(k)
                k += 1
                if int(k) == 91:
                    k = 65
                if int(k) == 123:
                    k = 97
            answer += chr(k)
    return answer