import sys
from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append([a,0])
    visit = [0 for i in range(100001)]
    visit[a] = 1
    if b <= a:
        print(a - b)
        return
    while queue:
        x , y = queue.popleft()
        if x == b:
            print(y)
            return
        else:
            if 0<=(x*2)<=100000 and visit[x*2] == 0:
                visit[x*2] = 1
                queue.append([x*2,y+1])
            if 0<=(x+1)<=100000 and visit[x+1] == 0:
                visit[x+1] = 1
                queue.append([x+1,y+1])
            if 0<=(x-1)<=100000 and visit[x-1] == 0:
                visit[x-1] = 1
                queue.append([x-1,y+1])
            
            
    

a, b = map(int,sys.stdin.readline().split())
bfs(a,b)