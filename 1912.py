import sys

n = int(sys.stdin.readline())
index = list(map(int,sys.stdin.readline().split()))

for i in range(1, n):
    index[i] = max(index[i], index[i] + index[i - 1])

print(max(index))