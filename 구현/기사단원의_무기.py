def solution(number, limit, power):
    answer = 0
    counts = 0
    for num in range(1, number + 1):
        for j in range(1, int(num**(1/2) + 1)):
            if num % j == 0:
                counts += 1
                if j**2 != num:
                    counts += 1
        answer += power if counts > limit else counts
        counts = 0
    return answer