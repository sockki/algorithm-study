import sys

max = 0
def dfs(leng,now=None):
    global max
    if now is None:
        now = []

    if leng == n:
        a = 0
        for i in range(n-1):
            a += abs(now[i] - now[i+1])
        if a > max:
            max = a
    
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            now.append(data[i])
            dfs(leng + 1, now)
            visit[i] = 0
            b = now.pop()


n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
visit = [0 for _ in range(n)]
some = []
dfs(0, some)
print(max)