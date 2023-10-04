import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visit = [0 for _ in range(n)]
    while queue:
        a,b = queue.popleft()
        if (abs(px - a) + abs(py - b)) <= 1000:
            print("happy")
            return
        else:
            for i in range(n):
                if (abs(pyun[i][0] - a) + abs(pyun[i][1] - b)) <= 1000 and visit[i] == 0:
                    visit[i] = 1
                    queue.append([pyun[i][0],pyun[i][1]])
        
    print("sad")


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    hx, hy = map(int,sys.stdin.readline().split())
    pyun = []
    result = []
    for j in range(n):
        pyun.append(list(map(int,sys.stdin.readline().split())))
    px, py = map(int,sys.stdin.readline().split())
    bfs(hx,hy)

    
    
