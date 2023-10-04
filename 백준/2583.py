import sys
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]


def bfs(x,y):
    queue = deque()
    queue.append([y,x])
    visit[y][x] = 1
    count = 1
    while queue:
        b,a = queue.popleft()
        for i in range(4):
            bb = b + dy[i]
            aa = a + dx[i]
            if 0<=aa<n and 0<=bb<m and not graph[bb][aa] and not visit[bb][aa]:
                count += 1
                visit[bb][aa] = 1
                queue.append([bb,aa])
    
    num.append(count)




m,n,k = map(int,sys.stdin.readline().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]
for i in range(k):
    a,b,c,d = map(int,sys.stdin.readline().split())
    for j in range(a,c):
        for l in range(b,d):
            graph[l][j] += 1

result = 0
num = []
for j in range(m):
    for i in range(n):
        if not graph[j][i] and not visit[j][i]:
            result += 1
            bfs(i,j)


num.sort()
print(result)
print(*num)

