import sys

n = int(sys.stdin.readline())
d=[]
dp1 = [[0,0,0]]
dp2 = [[0,0,0]]
result = []
for i in range(n):
    d.append(list(map(int,sys.stdin.readline().split())))
    dp1.append([max(d[0][0] + dp1[0][0],d[0][0] + dp1[0][1]),max(d[0][1] + dp1[0][0],d[0][1] + dp1[0][1],d[0][1] + dp1[0][2]),max(d[0][2] + dp1[0][1],d[0][2] + dp1[0][2])])
    dp1.pop(0)
    dp2.append([min(d[0][0] + dp2[0][0],d[0][0] + dp2[0][1]),min(d[0][1] + dp2[0][0],d[0][1] + dp2[0][1],d[0][1] + dp2[0][2]),min(d[0][2] + dp2[0][1],d[0][2] + dp2[0][2])])
    dp2.pop(0)
    d.pop(0)

print(max(dp1[0]),min(dp2[0]))




