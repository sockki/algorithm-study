from itertools import combinations, permutations

def solution(dots):
    answer = 0
    perm = list(permutations(dots,4))
    print(perm)
    for i in perm:
        if (i[0][1] - i[1][1])/(i[0][0] - i[1][0]) == (i[2][1] - i[3][1])/(i[2][0] - i[3][0]):
            return 1
        
    return answer