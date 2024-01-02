def solution(storey):
    result = 0
    while storey != 0:
        one_point = int(storey % 10)
        if one_point >= 6:
            storey += 10 - one_point
            result += 10 - one_point
        elif one_point == 5 and int((storey // 10) % 10) >= 5:
            storey += 5
            result += 5
        else:
            storey -= one_point
            result += one_point
            
        storey = storey // 10

                
    return result