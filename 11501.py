import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    result = 0
    data = []
    max = 0
    ju = list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        now = ju.pop()
        if now > max:
           max = now
        else:
            result -= now
            result += max
    
    print(result)
                    


    
    