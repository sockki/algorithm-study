def solution(triangle):
    dp = [[] for i in range(len(triangle))]
    dp[0].append(0)
    dp[0].append(triangle[0][0])
    dp[0].append(0)
    
    for i in range(1, len(triangle)):
        dp[i].append(0)
        for j in range(len(triangle[i])):
            dp[i].append(max(dp[i-1][j] + triangle[i][j], dp[i-1][j+1] + triangle[i][j]))
        dp[i].append(0)
                         
    
    return max(dp[len(triangle)-1])