import sys

n = int(sys.stdin.readline())


data = list(map(int,sys.stdin.readline().split()))
b , c = map(int,sys.stdin.readline().split())

result = 0
for i in range(n):
    if data[i] < b:
        result += 1
    elif int((data[i] - b) % c) == 0:
        result += int((data[i] - b) / c) + 1
    else:
        result += int((data[i] - b) / c) + 2
    

print(result)