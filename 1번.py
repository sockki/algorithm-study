from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    다음달받을선물 = defaultdict(int)
    주고받은 = defaultdict(dict)
    for friend in friends:
        주고받은[friend] = defaultdict(int)
    선물지수 = defaultdict(int)
    for gift in gifts:
        준, 받은 = gift.split(" ")
        주고받은[준][받은] += 1
        선물지수[준] += 1
        선물지수[받은] -= 1
    
    for i in range(len(friends) - 1):
        for j in range(i+1, len(friends)):
            if 주고받은[friends[i]][friends[j]] == 주고받은[friends[j]][friends[i]]:
                if 선물지수[friends[i]] == 선물지수[friends[j]]:
                    continue
                elif 선물지수[friends[i]] > 선물지수[friends[j]]:
                    다음달받을선물[friends[i]] += 1
                else :
                    다음달받을선물[friends[j]] += 1
            elif 주고받은[friends[i]][friends[j]] > 주고받은[friends[j]][friends[i]]:
                다음달받을선물[friends[i]] += 1
            else:
                다음달받을선물[friends[j]] += 1
    
        

    return max(list(다음달받을선물.values())) if list(다음달받을선물.values()) else 0