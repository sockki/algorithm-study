import sys

n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    data.sort()
    a = data.pop(0)
    b = data.pop(0)
    data.append(a+b)
    data.append(a+b)


print(sum(data))