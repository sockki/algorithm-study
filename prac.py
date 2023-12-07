from itertools import combinations

for i in range(5):
        case = list(combinations([0,1,2,3], i))
        for c in case:
            print(c)