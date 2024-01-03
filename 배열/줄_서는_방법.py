def solution(n, k):
    answer = []
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    while n != 0:
        pack = 1
        for i in range(1,n):
            pack = pack * i
        a = (k-1) // pack
        answer.append(arr.pop(a))
        k = int(k % pack)
        n -= 1
    
    
    return answer