from collections import deque


def solution(maps):
    answer = 0

    visit = [[0]*len(maps[0]) for i in range(len(maps))]

    def bfs(x, y):
        dx = [0, 0, -1, +1]
        dy = [1, -1, 0, 0]
        queue = deque()
        queue.append([y, x, 1])
        visit[y][x] = 1
        while queue:
            y, x, b = queue.popleft()
            if y == len(maps) - 1 and x == len(maps[0]) - 1:
                nonlocal answer
                answer = b
                return

            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < len(maps) and 0 <= xx < len(maps[0]) and visit[yy][xx] == 0 and maps[yy][xx] == 1:
                    visit[yy][xx] = 1
                    queue.append([yy, xx, b+1])
    bfs(0, 0)
    print(visit)

    if answer == 0:
        return -1

    return answer
