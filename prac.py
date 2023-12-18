from collections import deque

picks = [1, 3, 2]
minerals= ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

def solution(picks, minerals):
    result = []
    
    def dfs(picks, minerals, n, p):
        nonlocal result 
        
        if n == 0:
            picks[n] -= 1
            minerals = deque(minerals)
            for i in range(5):
                if minerals:
                    minerals.popleft()
                    p += 1
                    
        elif n == 1:
            picks[n] -= 1
            minerals = deque(minerals)
            for i in range(5):
                if minerals:
                    a = minerals.popleft()
                    if a == "diamond":
                        p += 5
                    else:
                        p += 1
        elif n == 2:
            picks[n] -= 1
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
                dfs(picks, minerals, 0, p)
            if picks[1] > 0:
                dfs(picks, minerals, 1, p)
            if picks[2] > 0:
                dfs(picks, minerals, 2, p)
                
    p = 0

    if picks[0] > 0:
        dfs(picks, minerals, 0, p)
    if picks[1] > 0:
        dfs(picks, minerals, 1, p)
    if picks[2] > 0:
        dfs(picks, minerals, 2, p)
        
    
        
        
    return result

print(solution(picks, minerals))