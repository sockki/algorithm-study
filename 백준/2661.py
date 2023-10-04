import sys

def check(result,count):
    for i in range(count):
        sli = result[i:]
        for i in range(1, len(sli)//2 + 1):
            a = sli[:i]
            b = sli[i:i+i]
            if a == b:
                return False
    
    return True

def back(count):
    if not check(result, count):
        return -1
    if count == n:
        print(*result, sep="")
        return 0
    for i in range(1,4):
        result.append(i)
        if back(count+1) == 0:
            return 0
        result.pop()


n = int(sys.stdin.readline())
result = []
back(0)


    