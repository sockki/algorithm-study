import sys
from collections import deque

def dfs(v):
    stack = []
    result = []
    stack.append(v - 1)

    while stack:
        now = stack.pop()
        if now not in result:
            result.append(now)
            for i in graph[now]:
                stack.append(i)


    return result

def bfs(v):
    queue = deque()
    result = []
    queue.append(v - 1)
    result.append(v - 1)

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if i not in result:
                queue.append(i)
                result.append(i)

    return result


n, m, v = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n)]
for j in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for k in range(n):
    graph[k].sort()

bfsr = bfs(v)

for k in range(n):
    graph[k].sort(reverse=True)

dfsr = dfs(v)


for i in dfsr:
    print(i + 1, end=" ")

print()
for i in bfsr:
    print(i + 1, end=" ")
