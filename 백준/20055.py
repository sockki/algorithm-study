import sys
from collections import deque

n , k = map(int,sys.stdin.readline().split())
belt = deque(list(map(int,sys.stdin.readline().split())))
robot = deque([0]*n)
t = 0
count = 0
while True:
    t += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    for i in reversed(range(n-1)):
        if robot[i] and belt[i+1] and not robot[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if not belt[i+1]:
                count += 1
    if not robot[0] and belt[0]:
        belt[0] -= 1
        robot[0] = 1
        if not belt[0]:
            count += 1
    robot[-1] = 0
    if count >= k:
        break

print(t)
