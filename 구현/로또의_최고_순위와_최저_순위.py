def solution(lottos, win_nums):
    answer = []
    unknown = lottos.count(0)
    num = 0
    for lotto in lottos:
        if lotto in win_nums:
            num += 1
    
    return [(7-(num+unknown) if num+unknown >= 1 else 6), (7-num if num >= 1 else 6)]