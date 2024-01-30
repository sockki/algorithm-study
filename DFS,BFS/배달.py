from collections import defaultdict
from collections import deque
def solution(N, road, K):
    answer = 0
    arr = set()
    dic = defaultdict(list)
    maxs = defaultdict(int)
    for i in range(1,N+1):
        maxs[i] = 0
        
    for r in road:
        dic[r[0]].append([r[1],r[2]])
        dic[r[1]].append([r[0],r[2]])
    queue = deque()
    queue.append([1,K])
    arr.add(1)
    while queue:
        now,distance = queue.popleft()
        arr.add(now)
        if distance == 0:
            continue
        for i in dic[now]:
            if distance >= i[1] and maxs[i[0]] <= distance - i[1]:
                queue.append([i[0], distance - i[1]])
                maxs[i[0]] = distance - i[1]
                
    return len(arr)