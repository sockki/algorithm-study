from collections import deque

def solution(picks, minerals):
    result = []
    
    def dfs(picks, minerals, n, p):
        nonlocal result 
        
        if n == 0:
            minerals = deque(minerals)
            for i in range(5):
                if minerals:
                    minerals.popleft()
                    p += 1
                    
        elif n == 1:
            minerals = deque(minerals)
            for i in range(5):
                if minerals:
                    a = minerals.popleft()
                    if a == "diamond":
                        p += 5
                    else:
                        p += 1
        elif n == 2:
            minerals = deque(minerals)
            for i in range(5):
                if minerals:
                    a = minerals.popleft()
                    if a == "diamond":
                        p += 25
                    elif a == "iron":
                        p += 5
                    else:
                        p += 1
        if sum(picks) == 0 or not minerals:
            result.append(p)
            return
        else:
            minerals = list(minerals)
            if picks[0] > 0:
                picks[0] -= 1
                dfs(picks, minerals, 0, p)
                picks[0] += 1
            if picks[1] > 0:
                picks[1] -= 1
                dfs(picks, minerals, 1, p)
                picks[1] += 1
            if picks[2] > 0:
                picks[2] -= 1
                dfs(picks, minerals, 2, p)
                picks[2] += 1
                
    p = 0

    if picks[0] > 0:
        picks[0] -= 1
        dfs(picks, minerals, 0, p)
        picks[0] += 1
    if picks[1] > 0:
        picks[1] -= 1
        dfs(picks, minerals, 1, p)
        picks[1] += 1
    if picks[2] > 0:
        picks[2] -= 1
        dfs(picks, minerals, 2, p)
        picks[2] += 1
    
        
        
    return min(result)

### 모범풀이

def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x
    
    # 캘 수 있는 광물의 개수
    num_min = sum * 5
    if len(minerals) > num_min: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:num_min]
        
    # 광물 조사
    cnt_min = [[0, 0, 0]for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # 피로도가 높은 순서대로 광물 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))
    
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
    
        
        
    return answer
