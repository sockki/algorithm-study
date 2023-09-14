import sys

def rotate(data=None):
    global Tom
    if data is None:
        data = []
    for i in range(4):
        if data[i] == 1:
            Tom[i] = Tom[i][7] + Tom[i][0:7]
        elif data[i] == -1:
            Tom[i] = Tom[i][1:] + Tom[i][0]



def reason():
    global Tom
    for i in range(k):
        result = [0,0,0,0]
        a = num[i]
        b = ro[i]
        if a == 1:
            result[0] = b
            if Tom[0][2] != Tom[1][6]:
                result[1] = -b
                if Tom[1][2] != Tom[2][6]:
                    result[2] = b
                    if Tom[2][2] != Tom[3][6]:
                        result[3] = -b
        elif a == 2:
            result[1] = b
            if Tom[0][2] != Tom[1][6]:
                result[0] = -b
            if Tom[1][2] != Tom[2][6]:
                result[2] = -b
                if Tom[2][2] != Tom[3][6]:
                    result[3] = b
        elif a == 3:
            result[2] = b
            if Tom[2][2] != Tom[3][6]:
                result[3] = -b
            if Tom[1][2] != Tom[2][6]:
                result[1] = -b
                if Tom[0][2] != Tom[1][6]:
                    result[0] = b
        elif a == 4:
            result[3] = b
            if Tom[2][2] != Tom[3][6]:
                result[2] = -b
                if Tom[1][2] != Tom[2][6]:
                    result[1] = b
                    if Tom[0][2] != Tom[1][6]:
                        result[0] = -b
        rotate(result)





Tom = [sys.stdin.readline().rstrip() for _ in range(4)]
k = int(sys.stdin.readline())
num = []
ro = []
for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    num.append(a)
    ro.append(b)

reason()
ans = 0
for i in range(4):
    if Tom[i][0] == '1':
        ans += 2**i

print(ans)