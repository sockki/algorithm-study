import sys

p = []
t = []
r = []
n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    t.append(a)
    p.append(b)
result = []
index = 2
now = True
if(t[0] > 1):
    r.append(0)
else:
    r.append(p[0])

while index < n+1:
    result = []
    for i in range(index,0,-1):
        if ((i - 1) + t[i - 1]) == index:
            result.append(p[i - 1] + r[i - 2])
            now = False
    if now == True:
        r.append(r[index - 2])
    else:
        r.append(max(max(result),r[index - 2]))
    index += 1
    now = True

print(r[n-1])

#풀지못했음