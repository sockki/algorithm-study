import sys

count = 0
def dfs(sep, gil):
    global count
    if gil == n:
        return
    sep += data[gil]
    gil += 1
    if sep == s:
        count += 1
    dfs(sep, gil)
    gil -= 1
    sep -= data[gil]
    gil += 1
    dfs(sep, gil)


n,s = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

dfs(0,0)


print(count)