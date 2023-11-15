from collections import deque

def solution(A, B):
    answer = 0
    queue1 = deque(A)
    queue2 = deque(B)
    while queue1 != queue2:
        if answer == len(A):
            answer = -1
            break
        x = queue1.pop()
        queue1.appendleft(x)
        answer += 1
    return answer