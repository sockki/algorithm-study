def solution(n, results):
    answer = 0
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for result in results:
        a,b = result
        grid[a-1][b-1] = 1
    for i in range(n):    # 거치는 점
        for k in range(n):   # 시작점
            for j in range(n):  # 끝점
                if grid[k][i] == 1 and grid[i][j] == 1:
                    grid[k][j] = 1
    answers = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                answers[i] += 1
                answers[j] += 1
    
    for a in answers:
        if a == n - 1:
            answer += 1
    return answer

# 플루이드-워셜 모든 정점들 사이의 가장 짧은 거리를 찾는 알고리즘
# 1. 하나의 정점에서 다른 정점으로 바로 갈 수 있다면 최소 비용을, 갈 수없다면 INF로 배열에 저장
# 2. 3중 for문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우 값을 교체
# 3. 2번의 과정을 반복해 모든 정점사이의 최단 경로를 탐색