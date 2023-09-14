import sys

def dfs(data=None):
    if data is None:
        data = []
    global alist, b, isTrue, result
    if len(data) == len(alist):
        c = int(''.join(s for s in data))
        if data[0] != '0' and c < b:
            result.append(c)
            return
    else:
        for i in range(len(isTrue)):
            if isTrue[i] == False:
                isTrue[i] = True
                data.append(alist[i])
                dfs(data)
                data.pop()
                isTrue[i] = False


a, b = map(int,sys.stdin.readline().split())
a = str(a)
alist = list(a)
isTrue = [False for i in range(len(alist))]
c = []
result = []
dfs(c)
if result:
    print(max(result))
else:
    print(-1)






