import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

data = []
n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().split()) for i in range(n)]

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                queue.append([i, j])
    
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            aa = a + dx[i]
            bb = b + dy[i]
            while 0<=aa<n and 0<=bb<n :
                if data[aa][bb] == 'O':
                    break
                if data[aa][bb] == 'S':
                    return False
                aa += dx[i]
                bb += dy[i]
    
    return True


def recursive(cnt):
    global result
    if cnt == 3:
        cantsearch = bfs()
        if cantsearch:
            result = "YES"
            return
        else:
            return
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                recursive(cnt + 1)
                data[i][j] = 'X'



result = "NO"
recursive(0)
print(result)



        