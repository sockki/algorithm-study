from collections import deque


def solution(n, computers):
    answer = 0
    visit = [0] * n

    def bfs(now):
        queue = deque()
        queue.append(now)
        while queue:
            now = queue.popleft()
            for idx, computer in enumerate(computers[now]):
                if idx != now and computer and not visit[idx]:
                    visit[idx] = 1
                    queue.append(idx)

        return 1

    for i in range(n):
        if not visit[i]:
            answer += bfs(i)

    return answer
