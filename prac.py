from collections import deque
from itertools import combinations

maxround = 0

def dfs(mycard, cards, coin, rounds, number):
    global maxround
    if maxround < rounds:
        maxround = rounds
    if not cards:
        return
    cards = deque(cards)
    a = cards.popleft()
    b = cards.popleft()
    if coin >= 2:
        coin -= 2
        mycard.append(a)
        mycard.append(b)
        combi = list(combinations(mycard, 2))
        for c in combi:
            if c[0] + c[1] == number:
                mycard.remove(c[0])
                mycard.remove(c[1])
                cards = list(cards)
                dfs(mycard, cards, coin, rounds + 1, number)
        mycard.pop()
        mycard.pop()
    if coin >= 1:
        coin -= 1
        mycard.append(a)
        combi = list(combinations(mycard, 2))
        for c in combi:
            if c[0] + c[1] == number:
                mycard.remove(c[0])
                mycard.remove(c[1])
                cards = list(cards)
                dfs(mycard, cards, coin, rounds + 1, number)
        mycard.pop()
    combi = list(combinations(mycard, 2))
    for c in combi:
        if c[0] + c[1] == number:
            mycard.remove(c[0])
            mycard.remove(c[1])
            cards = list(cards)
            dfs(mycard, cards, coin, rounds + 1, number)


        

def solution(coin, cards):
    n = len(cards)
    mycard = []
    cards = deque(cards)
    for i in range(n//3):
        a = cards.popleft()
        mycard.append(a)

    cards = list(cards)
    dfs(mycard, cards, coin, 1, n+1)
    
    return maxround


lkl = solution(4,[3,6,7,2,1,10,5,9,8,12,11,4])
print(lkl)