import sys
now = list(sys.stdin.readline().strip())
num = int(sys.stdin.readline())
command = [sys.stdin.readline().strip() for i in range(num)]
aft = []


for i in range(num):
    if command[i].find("L") >= 0:
        if not now:
            continue
        aft.append(now.pop())
       

    elif command[i].find("D") >= 0:
        if not aft:
            continue
        now.append(aft.pop())
        

    elif command[i].find("B") >= 0:
        if not now:
            continue
        nob = now.pop()
        

    elif command[i].find("P") >= 0:
        now.append(command[i][2:])

aft.reverse()
result = now + aft
print(''.join(result))




