import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

dp = [[0] for _ in range(n)]
dp[0][0] = data[0][0]
for i in range(2,n+1):
    for j in range(i):
        if j == 0:
            dp[i-1][0] = dp[i-2][0] + data[i-1][0]
        elif j == i-1:
            dp[i-1].append(dp[i-2][j-1] + data[i-1][j])
        else:
            dp[i-1].append(max(dp[i-2][j-1] + data[i-1][j] ,dp[i-2][j] + data[i-1][j] ))

print(max(dp[n-1]))
        
