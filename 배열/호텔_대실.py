def solution(book_time):
    answer = 0
    newtime = []
    for i in book_time:
        a,b = i[0].split(":")
        c,d = i[1].split(":")
        starttime = int(b) + int(a)*60
        endtime = int(d) + (int(c)*60) + 10
        newtime.append([starttime,endtime])
    
    newtime.sort(key=lambda x : x[0])
    dic = {}
    diclen = 1
    dic[0] = newtime[0]
    for i in range(1, len(newtime)):
        intime = False
        for j in range(diclen):
            if dic[j][1] <= newtime[i][0]:
                dic[j] = newtime[i]
                intime = True
                break
        if not intime:
            diclen += 1
            dic[diclen-1] = newtime[i]
                
            
    return diclen