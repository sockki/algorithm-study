from itertools import product


def solution(word):
    alp = ["A","E","I","O","U"]
    words = []
    for i in range(1,6):
        for j in product(alp, repeat=i):
            words.append("".join(list(j)))
    
    words.sort()
    
    for i in range(len(words)):
        if words[i] == word:
            return i + 1
            
    return answer