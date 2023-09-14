import sys
from collections import deque


def bfs(a):
    queue = deque()
    queue.append(a)
    visit[a] = 1
    while queue:
        now = queue.popleft()
        for i in data[now]:
            if not visit[i]:
                visit[i] = 1
                queue.append(i)

    return 1


n, m = map(int, sys.stdin.readline().split())
data = [[] for _ in range(n)]
visit = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    data[a-1].append(b-1)
    data[b-1].append(a-1)

result = 0
for i in range(n):
    if not visit[i]:
        result += bfs(i)

print(result)
