def solution(alp, cop, problems):
    answer = 0
    maxalp = max(map(lambda x:x[0], problems))
    maxcop = max(map(lambda x:x[1], problems))
    maxalp = max(alp, maxalp)
    maxcop = max(cop, maxcop)
    
    dp = [[160 for i in range(maxcop + 1)] for i in range(maxalp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, maxalp + 1):
        for j in range(cop, maxcop + 1):
            if i + 1 <= maxalp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= maxcop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(i + alp_rwd, maxalp), min(j + cop_rwd, maxcop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
    
    return dp[-1][-1]

# 각기 다른 경우에 최솟값을 구하며, 그 양이 방대할 경우 무조건 dp 사용
# 값이 2개인 경우 그거에 맞추어서 dp 사용