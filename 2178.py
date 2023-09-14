import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    queue = deque()
    field[0][0] = 0
    queue.append([0,0,1])
    while queue:
        y, x, i = queue.popleft()
        for a in range(4):
            xx = x + dx[a]
            yy = y + dy[a]
            if xx == m - 1 and yy == n - 1:
                print(i + 1)
                return
            elif (0 <= xx < m) and (0 <= yy < n) and field[yy][xx] == 1:
                field[yy][xx] = 0
                queue.append([yy, xx, i + 1])

n, m = map(int, sys.stdin.readline().split())
field = []
for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().rstrip())))

bfs()

