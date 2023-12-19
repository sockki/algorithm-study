def solution(k, dungeons):
    answer = -1
    result = []
    visit = [0 for i in range(len(dungeons))]
    def dfs(k, dungeons, visit, n):
        nonlocal answer
        if answer < n:
            answer = n
        for i in range(len(dungeons)):
            if not visit[i] and dungeons[i][0] <= k:
                visit[i] = 1
                k -= dungeons[i][1]
                dfs(k, dungeons, visit, n + 1)
                visit[i] = 0
                k += dungeons[i][1]
        
        
    dfs(k, dungeons, visit, 0)
    
    return answer