from collections import defaultdict
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    maps = defaultdict(list)
    for road in roads:
        maps[road[0]].append(road[1])
        maps[road[1]].append(road[0])
        
    queue = deque()
    visit = set()
    distance = [-1 for i in range(n+1)]
    queue.append([destination,0])
    while queue:
        a,b = queue.popleft()
        if a in visit:
            continue
        visit.add(a)
        distance[a] = b
        for m in maps[a]:
            queue.append([m,b+1])
            
    for source in sources:
        answer.append(distance[source])
        
    return answer