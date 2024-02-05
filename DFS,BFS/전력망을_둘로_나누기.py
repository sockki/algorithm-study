from collections import defaultdict
from collections import deque


def solution(n, wires):
    answer = 200
    dic = defaultdict(list)
    for wire in wires:
        dic[wire[0]].append(wire[1])
        dic[wire[1]].append(wire[0])
        
    def bfs(start,end):
        queue = deque()
        visit = [0 for i in range(n + 1)]
        queue.append(start)
        visit[start] = 1
        ans = 1
        while queue:
            a = queue.popleft()
            for i in dic[a]:
                if i != end and not visit[i]:
                    visit[i] = 1
                    queue.append(i)
                    ans += 1
        return ans
                    
    for wire in wires:
        first = bfs(wire[0],wire[1])
        second = bfs(wire[1],wire[0])
        if abs(first-second) < answer:
            answer = abs(first-second)
    
    
    return answer