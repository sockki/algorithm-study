def solution(k, ranges):
    answer = []
    수열 = []
    정적분 = []
    수열.append([0,k])
    idx = 0
    
    while k > 1:
        idx += 1
        if k % 2 == 0:
            k = k // 2
            수열.append([idx,k])
        else:
            k = (k * 3) + 1
            수열.append([idx,k])
    for i in range(len(수열) - 1):
        miny = min([수열[i][1], 수열[i+1][1]])
        정적분.append(miny + (abs(수열[i][1]-수열[i+1][1]) / 2))

    n = len(수열) - 1
    for r in ranges:
        a = r[0]
        b = r[1] if r[1] > 0 else n + r[1]
        if a > b:
            answer.append(-1)
        else:
            answer.append(sum(정적분[a:b]))
    return answer