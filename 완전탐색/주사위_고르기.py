from itertools import combinations,product
from bisect import bisect_left

def solution(dice):
    answer = []
    n = len(dice)
    arr = [i for i in range(n)]
    combi = list(combinations(arr, int(n/2)))
    maxwin = 0
    maxteam = []
    while combi:
        now = combi.pop(0)
        now = list(now)
        nowteam = []
        opteam = []
        for i in arr:
            if i not in now:
                opteam.append(dice[i])
            else:
                nowteam.append(dice[i])
        nowwin = 0
        products = list(product([0,1,2,3,4,5], repeat=int(n/2)))
        nowteamresult = []
        opteamresult = []
        for pro in products:
            nowteamresult.append(sum(nowteam[i][pro[i]] for i in range(int(n/2))))
            opteamresult.append(sum(opteam[i][pro[i]] for i in range(int(n/2))))
        opteamresult.sort()
        
        for result in nowteamresult:
            nowwin += bisect_left(opteamresult, result)
            
        if nowwin > maxwin:
            maxwin = nowwin
            maxteam = [i + 1 for i in now]
    return maxteam

#bitsect 을 사용해보자