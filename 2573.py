import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs(n,m):
    queue = deque()
    queue.append([n,m])
    sea = []
    visit[n][m] = 1
    while queue:
        y,x = queue.popleft()
        count = 0
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < a and 0 <= xx < b:
                if not graph[yy][xx]:
                    count += 1
                elif not visit[yy][xx] and graph[yy][xx]:
                    visit[yy][xx] = 1
                    queue.append([yy,xx])
        if count > 0:
            sea.append([y,x,count])
    
    for k,l,c in sea:
        graph[k][l] = max(0,graph[k][l] - c)
    
    return 1



    

a,b = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(a)]
ice = []
for i in range(a):
    for j in range(b):
        if graph[i][j]:
            ice.append((i, j))

day = 0
while ice:
    con = 0
    delList = []
    visit = [[0] * b for _ in range(a)]
    for i,j in ice:
        if graph[i][j] and not visit[i][j]:
            con += bfs(i,j)
        if graph[i][j] == 0:
            delList.append((i,j))
    if con > 1:
        print(day)
        break
    ice = sorted(list(set(ice) - set(delList)))
    day += 1

if con < 2:
    print(0)
    

                

