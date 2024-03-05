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