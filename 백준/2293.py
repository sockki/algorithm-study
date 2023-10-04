import sys



n,k = map(int,sys.stdin.readline().split())
dong = []
for i in range(n):
    dong.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
dp[0] = 1
# dp[i] -> i원을 만들 때 가능한 경우의 수
# dp[0] -> 동전 하나를 사용하는 경우 (coin이 3일 때, dp[3 - 3] = 1로 맞춰줌으로써 0원에서 3원을 더해 3원을 만드는 경우라고 생각)

for d in dong:
    for i in range(d , k+1):
        dp[i] += dp[i - d]

print(dp[k])