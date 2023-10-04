import sys
from collections import deque

def bfs(f,s,g,u,d):
    queue = deque()
    visit = [0 for _ in range(f)]
    visit[s-1] = 1
    queue.append([s,0])
    while queue:
        a , b = queue.popleft()
        if a == g:
            print(b)
            return
        if a - d > 0 and visit[a-d-1] == 0:
            visit[a-d-1] = 1
            queue.append([a-d, b+1])
        if a + u <= f and visit[a+u-1] == 0:
            visit[a+u-1] = 1
            queue.append([a+u,b+1])
    
    print("use the stairs")


f,s,g,u,d = map(int,sys.stdin.readline().split())
bfs(f,s,g,u,d)

