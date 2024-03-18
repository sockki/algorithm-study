def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    link = set([costs[0][0]])
    
    while len(link) < n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:
                continue
            elif cost[0] in link or cost[1] in link:
                link.update([cost[0],cost[1]])
                answer += cost[2]
                break
            
    return answer


# 크루스칼: 그래프의 정점들을 최소 비용으로 모두 연결하는 알고리즘
# 1. 그래프의 간선을 오름차순으로 연결
# 2. 순서대로 사이클을 형성하지 않는 간선을 선택(집합을 사용해 두 정점이 같은 집합에 속해 있지 않는지 판단)
# 3. 집합에 모든 정점이 속하면 정지
