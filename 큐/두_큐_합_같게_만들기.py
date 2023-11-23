from collections import deque

def solution(queue1, queue2):
    answer = 0
    maxl = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    tot = tot1 + tot2
    
    if tot % 2 != 0:
        return -1
    
    while answer < maxl:
        if tot1 == tot2:
            break
        else:
            answer += 1
            if tot1 > tot2:
                a = queue1.popleft()
                queue2.append(a)
                tot1 -= a
                tot2 += a
            else:
                a = queue2.popleft()
                queue1.append(a)
                tot2 -= a
                tot1 += a
    return answer if answer < maxl else -1

# 두 큐가 원래 자리로 오려면 4번 반복해야함
# sum 함수는 시간이 오래걸린다. 되도록 사용하지 않도록 하자