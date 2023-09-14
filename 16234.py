import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = []
def bfs(a,b):
    global result,visit,trick
    part = []
    queue = deque()
    visit[a][b] = 1
    queue.append([a,b])
    part.append([a,b])
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<=xx<n and 0<=yy<n and visit[yy][xx] == 0 and l<=abs(data[y][x] - data[yy][xx])<=r:
                visit[yy][xx] = 1
                part.append([yy,xx])
                queue.append([yy, xx])
                if trick == False:
                    trick = True
    if len(part) > 1:
        result.append(part)

def made(result=None):
    if result is None:
        result = []
    for i in result:
        sum=0
        count=0
        for y,x in i:
            sum += data[y][x]
            count += 1
        sum = int(sum / count)
        for y,x in i:
            data[y][x] = sum
        
            





n,l,r = map(int,sys.stdin.readline().split())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
day = 0
trick = True
while trick:
    result = []
    trick = False
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                bfs(i,j)
    if trick == True:
        made(result)
        day += 1

print(day)
    

