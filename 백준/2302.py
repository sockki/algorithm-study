import sys


n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
m = int(sys.stdin.readline())
vip = []
for i in range(m):
    vip.append(int(sys.stdin.readline()))

dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    if i in vip:
        dp[i] = dp[i-1]
    elif i-1 in vip:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]


print(dp[n])

