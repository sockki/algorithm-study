from collections import deque

def solution(priorities, location):
    answer = 0
    process = []
    for i in range(len(priorities)):
        process.append(i)
        
    process = deque(process)
    priorities = deque(priorities)
    maxpro = max(priorities)
    count = 0
    while True:
        a = priorities.popleft()
        b = process.popleft()
        if a < maxpro:
            priorities.append(a)
            process.append(b)
        else:
            count += 1
            if b == location:
                return count
            maxpro = max(priorities)
    
        