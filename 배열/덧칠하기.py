def solution(n, m, section):
    answer = 0
    while section:
        now = section.pop(0)
        answer += 1
        while section and now + (m-1) >= section[0]:
            section.pop(0)
                
    return answer