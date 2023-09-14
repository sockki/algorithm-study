import sys




def dfs(i, arr):
    global maxval, minval, add, sub, mul, seq
    if i == n:
        maxval = max(maxval, arr)
        minval = min(minval, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        if seq > 0:
            seq -= 1
            dfs(i+1, int(arr / data[i]))
            seq += 1
            

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

add, sub, mul, seq = map(int, sys.stdin.readline().split())

maxval = -1e9
minval = 1e9

dfs(1, data[0])

print(maxval)
print(minval)
