import sys
from collections import deque

def bfs(a,b):
    queue = deque()
    visit = [False for _ in range(n)]
    queue.append([a,0])
    visit[a] = True
    while queue:
        x,y = queue.popleft()
        if x == b:
            print(y)
            return
        else:
            for i in graph[x]:
                if visit[i] == False:
                    visit[i] = True
                    queue.append([i,y+1])
    
    print(-1)

n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

bfs(a-1,b-1)