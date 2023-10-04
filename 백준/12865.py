import sys

data = [[0,0]]
n,k = map(int,sys.stdin.readline().split())
knap = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    data.append([a,b])

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = data[i][0]
        value = data[i][1]

        if j < weight:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(value+knap[i-1][j-weight],knap[i-1][j])

print(knap[n][k])

