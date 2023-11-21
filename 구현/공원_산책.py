move = {"E":[0,1], "W":[0,-1], "S":[1,0], "N":[-1,0]}
    
def solution(park, routes):
    answer = []
    W = len(park[0])
    H = len(park)
    def moving(route,y,x):
        nonlocal W, H
        loc,num = map(str,route.split())
        num = int(num)
        now = [y,x]
        for i in range(num):
            now[0] += move[loc][0]
            now[1] += move[loc][1]
            if 0<=now[0]<H and 0<=now[1]<W and park[now[0]][now[1]] != "X":
                continue
            else:
                return [y,x]
            
        return now

    for i in range(H):
        tt = False
        for j in range(W):
            if park[i][j] == "S":
                answer = [i,j]
                tt = True
                break
        if tt:
            break

                
    for i in routes:
        answer = moving(i,answer[0],answer[1])
    
    return answer