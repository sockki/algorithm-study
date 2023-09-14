import sys

n = int(sys.stdin.readline())
data = [0] * 10000
dp = [0] * 10000
for i in range(n):
    data[i] = int(sys.stdin.readline())

dp[0] = data[0]
dp[1] = data[1] + data[0]
dp[2] = max(data[0] + data[2], data[1]+data[2], dp[1])
for i in range(3, n):
    dp[i] = max(data[i] + dp[i-2], data[i] + data[i-1] +  dp[i-3], dp[i-1])

print(dp[n-1])