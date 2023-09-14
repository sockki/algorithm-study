import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
lengths = []
for i in range(n - 1):
    lengths.append(data[i + 1] - data[i])
lengths.sort()
result = 0
for i in range(n-k):
    result += lengths[i]

print(result)