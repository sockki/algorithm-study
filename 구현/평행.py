from itertools import combinations, permutations

def inclination(point1, point2):
    return (point2[1] - point1[1]) / (point2[0] - point1[0])


def solution(dots):
    combs = combinations(dots, 2)

    for comb in combs:
        another = [dot for dot in dots if dot not in comb]

        if inclination(*comb) == inclination(*another):
            return 1
    
        
    return 0

# dot for dot in dots if dot not in comb