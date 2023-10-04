import sys
from collections import deque

def bfs():
    queue = deque([0])
    visited[0] = True
    result = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result += 1

    return result

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b - 1)
    graph[b-1].append(a - 1)

answer = bfs()
print(answer)
