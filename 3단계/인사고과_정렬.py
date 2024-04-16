def solution(scores):
    if len(scores) == 1:
        return 1
    wanho = scores[0]
    others = scores[1:]
    wanho_sum = wanho[0] + wanho[1]
    others_sort = sorted(others, key= lambda x : (-x[0], -x[1]))
    first = others_sort[0]
    order = 1
    nexto = first
    for other in others_sort:
        if other[0] < nexto[0]:
            first = nexto
            
        if other[0] < first[0] and other[1] > first[1] and other[1] > nexto[1]:
            nexto = other
            
        if other[0] < first[0] and other[1] < first[1]:
            continue
            
        if wanho_sum < (other[0] + other[1]):
            if wanho[0] < other[0] and wanho[1] < other[1]:
                return -1
            else:
                order += 1
        
    return order