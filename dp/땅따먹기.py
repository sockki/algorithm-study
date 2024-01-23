def solution(land):
    dp = [[0,0,0,0] for _ in range(len(land))]
    dp[0][0] = land[0][0]
    dp[0][1] = land[0][1]
    dp[0][2] = land[0][2]
    dp[0][3] = land[0][3]
    
    for i in range(1, len(land)):
        for j in range(4):
            arr = [dp[i-1][k] for k in range(4) if k != j]
            dp[i][j] = max(arr) + land[i][j]
        
    

    return max(dp[len(land)-1])