import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    cnt = 0
    visited = [0 for i in range(N)]
    visited[start] = 1

    while queue:
        now = queue.popleft()
        for i in connect[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1

    return cnt


N, M = map(int, sys.stdin.readline().split())
connect = [[] for j in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    connect[b-1].append(a - 1)

# result 에서 + 1 하기
max = 0
maxnode = []
for i in range(N):
    now = bfs(i)
    if now > max:
        max = now
        maxnode.clear()
        maxnode.append(i)
    elif now == max:
        maxnode.append(i)

for i in maxnode:
    print(i + 1 , end=" ")
