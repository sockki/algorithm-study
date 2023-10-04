import sys
from collections import deque

result = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(len,x,y):
    global result, visit
    if len == k:
        if x == c-1 and y == 0:
            result += 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<c and 0<=yy<r and visit[yy][xx] == 0 and data[yy][xx] != "T":
            visit[yy][xx] = 1
            dfs(len + 1, xx, yy)
            visit[yy][xx] = 0
    



r,c,k = map(int,sys.stdin.readline().split())
data = [sys.stdin.readline().strip() for _ in range(r)] 
visit = [[0 for i in range(c)] for i in range(r)]
visit[r-1][0] = 1
dfs(1,0,r-1)

print(result)
