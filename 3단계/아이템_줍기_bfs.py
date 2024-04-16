from collections import deque


def bfs(y,x,d1,d2):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append([y,x,0])
    visit = [[0 for i in range(102)] for i in range(102)]
    visit[y][x] = 1
    while queue:
        a,b,c = queue.popleft()
        if a == d1 and b == d2:
            result.append(c // 2)
        else:
            for i in range(4):
                yy = a + dy[i]
                xx = b + dx[i]
                if not visit[yy][xx] and graph[yy][xx] == 1:
                    queue.append([yy,xx,c+1])
                    visit[yy][xx] = 1
            

def solution(rectangle, characterX, characterY, itemX, itemY):
    global graph, result
    index = 1
    result = []
    graph = [[0 for i in range(102)] for i in range(102)]
    for r in rectangle:
        makeroad(r[1]*2,r[0]*2,r[3]*2,r[2]*2)
    
    bfs(characterY*2,characterX*2,itemY*2,itemX*2)
                
    return min(result)

def makeroad(y1,x1,y2,x2):
    
    for yy in range(y1,y2+1):
        for xx in range(x1, x2+1):
            if (xx == x1 or xx == x2 or yy == y1 or yy == y2) and graph[yy][xx] != -1:
                graph[yy][xx] = 1
            else:
                graph[yy][xx] = -1
                
# 좌표 2배 해버리기
# visit를 경로로 쓰는 것도 앞으로 해보자