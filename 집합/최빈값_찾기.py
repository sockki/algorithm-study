def solution(array):
    while len(array) != 0:
        for i, n in enumerate(set(array)):
            array.remove(n)
        if i == 0: return n
    
    return -1
