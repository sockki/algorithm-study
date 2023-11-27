from collections import defaultdict
from collections import deque
# 가는 곳이 하나도 없는 정점: 막대 정점의 끝 
# 가는 곳이 두개이며 자신에게 돌아오는 정점: 8자 그래프
# 가는 곳이 두개 이상인 정점: 생성한 정점
# 가는 곳이 한개이며 자신에게 돌아오는 정점: 도넛 정점



def solution(edges):
    answer = []
    stick = 0
    donut = 0
    eight = 0
    graph = defaultdict(list)
    overtwo = False
    maxnum = 0
    for edge in edges:
        a,b = edge
        graph[a].append(b)
        if maxnum < max(a,b):
            maxnum = max(a,b)

    eight_graph_point = []
    for point in range(1, maxnum + 1):
        if len(graph[point]) >= 2:
            if len(graph[point]) >= 3:
                answer.append(point)
                overtwo = False
            else:
                eight_graph_point.append(point)
        elif len(graph[point]) == 0:
            stick += 1

        

    if not overtwo:
        if len(eight_graph_point) == 1:
            answer.append(eight_graph_point[0])
            eight_graph_point= []
        for point in eight_graph_point:
            queue = deque()
            queue.append(point)
            while queue:
                search = False
                now = queue.popleft()
                if graph[now][0] in eight_graph_point:
                    search = True
                    break
                if search:
                    answer.append(point)
                    eight_graph_point.remove(point)
                    break




                    
    eight = len(eight_graph_point)
    donut = len(graph[answer[0]]) - eight - stick

    answer.append(donut)
    answer.append(stick)
    answer.append(eight)

    return answer