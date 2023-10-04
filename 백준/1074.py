import sys

def boon(n,x,y):
    global result
    if n == 0:
        return
    if x > 2**(n-1):
        if y > 2**(n-1):
            result += ((2**(n-1))**2)*3
            boon(n-1,x-2**(n-1),y-2**(n-1))
        else:
            result += ((2**(n-1))**2)*1
            boon(n-1,x-2**(n-1),y)
    else:
        if y > 2**(n-1):
            result += ((2**(n-1))**2)*2
            boon(n-1,x,y-2**(n-1))
        else:
            result += ((2**(n-1))**2)*0
            boon(n-1,x,y)

n,r,c = map(int,sys.stdin.readline().split())
result = 0
boon(n,c+1,r+1)
print(result)

