import sys



n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
if(n == 1):
    print(d[0]+d[1]+d[2]+d[3]+d[4]+d[5] - max(d))
else:
    thresult = [d[0]+d[1]+d[2],d[0]+d[2]+d[4],d[0]+d[3]+d[4],d[0]+d[3]+d[1],d[5]+d[1]+d[2],d[5]+d[2]+d[4],d[5]+d[3]+d[4],d[5]+d[3]+d[1]]
    seresult = [d[0]+d[1],d[0]+d[2],d[0]+d[3],d[0]+d[4],d[3]+d[4],d[4]+d[2],d[1]+d[2],d[1]+d[2],d[1]+d[3],d[5]+d[1],d[5]+d[2],d[5]+d[3],d[5]+d[4]]
    onemin = min(d)
    semin = min(seresult)
    thmin = min(thresult)
    print(4*thmin + ((n-1)*4 + (n-2)*4)*semin + ((n-2)*(n-2)*5 + (n-2)*4)*onemin)
