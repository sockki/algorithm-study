from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    def get_min_intensity():
        pq = []
        visited = [100000001] * (n + 1)
        
        for gate in gates:
            visited[gate] = 0
            heappush(pq, (0, gate))
        
        while pq:
            intensity, node = heappop(pq)
            
            if node in summits_set or intensity > visited[node]:
                continue
                
            for weight, next_node in graph[node]:
                # next_node 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
                # 출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음
                new_intensity = max(weight, intensity)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq, (new_intensity, next_node))
        
        min_intensity = [0, 100000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
                
        return min_intensity
    
    summits.sort()
    summits_set = set(summits)
    graph = defaultdict(list)
    for i , j , w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    return get_min_intensity()

# 다익스트라 알고리즘: 간선가 노드가 주어질 때 하나의 정점으로 부터 시작해 모든 다른 정점까지의 최단경로 찾기

import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances