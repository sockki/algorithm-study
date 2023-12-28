

def solution(r1, r2):
    answer = 0
    r_1 = r1**2
    r_2 = r2**2
    for i in range(r1):
        answer += int((r_2 - i**2)**(0.5)) - int((r_1 - i**2 - 1)**(0.5))
    for i in range(r1, r2):
        answer += int((r_2 - i**2)**(0.5))
    
        
    return answer*4




