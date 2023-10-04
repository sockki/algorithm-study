import sys

n = int(sys.stdin.readline())
red = []
green = []
blue = []

for i in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    red.append(a)
    green.append(b)
    blue.append(c)

result = [[] for j in range(3)]
result[0].append(red[0])
result[1].append(green[0])
result[2].append(blue[0])
for i in range(1,n):
    for j in range(3):
        if j == 0:
            result[j].append(min(result[1][i-1], result[2][i-1]) + red[i])
        elif j == 1:
            result[j].append(min(result[0][i-1], result[2][i-1]) + green[i])
        else:
            result[j].append(min(result[0][i-1], result[1][i-1]) + blue[i])

print(min(result[0][n-1], result[1][n-1], result[2][n-1]))
