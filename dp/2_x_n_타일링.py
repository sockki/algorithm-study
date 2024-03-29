from collections import defaultdict
def solution(n):
    dp = defaultdict(int)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    
    return dp[n]