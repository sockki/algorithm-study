import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    graph[a][b] = '2'
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 1:
                graph[xx][yy] = 2
                count += 1
                queue.append([xx,yy])
    
    result.append(count)
    


n = int(sys.stdin.readline())
result = []
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            bfs(a,b)

print(len(result))
result.sort()
for i in result:
    print(i)

