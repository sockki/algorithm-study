import sys

n = int(sys.stdin.readline())
m = n - 1
dan = []
for i in range(n):
    dan.append(int(sys.stdin.readline())) 

dp = [[0,0] for i in range(n)]

for i in range(n):
    if(i == 0):
        dp[i][1] = dan[m - i]
    elif(i == 1):
        dp[i][1] = dan[m - i] + dan[m]
    elif(i == 2):
        dp[i][0] = dan[m - i] + dan[m]
    else:
        dp[i][0] = max(dp[i-2]) + dan[m - i]
        dp[i][1] = dp[i - 1][0] + dan[m - i]

result = [dp[m][0],dp[m][1],dp[m-1][1]]
print(max(result))