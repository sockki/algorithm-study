def solution(n):
    answer = ''
    nums = []
    while n > 0:
        rest = int(n % 3)
        if rest == 0:
            rest = 3
            n = (n // 3) - 1
            nums.append(rest)
        else:
            n = (n // 3)
            nums.append(rest)
            
    while nums:
        a = nums.pop()
        if a == 1:
            answer += "1"
        elif a == 2:
            answer += "2"
        elif a == 3:
            answer += "4"
        
    return answer