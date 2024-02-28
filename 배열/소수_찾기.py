import math

def solution(n):
    answer = 0
    arr = [True for _ in range(n+1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    for i in arr:
        if i:
            answer += 1
    return answer - 2

# 에라토스테네의 체