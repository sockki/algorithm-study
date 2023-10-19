#내가 처음에 짠 코드
def solution(tickets):
    answer = ["ICN"]
    visit = [0 for i in range(len(tickets))]
    result = []

    def dfs(now,tickets,visit,answer):
        if answer is None:
            answer = []
    
    
        if 0 not in visit:
            result.append(answer)
            return 
    
        for i in range(len(tickets)):
            if not visit[i] and tickets[i][0] == now:
                answer.append(tickets[i][1])
                visit[i] = 1
                dfs(tickets[i][1],tickets,visit,answer)
                visit[i] = 0
                answer.pop()
            
    dfs("ICN",tickets,visit,answer)

    result.sort()

    return result[0]

#정답코드

def solution(tickets):
    answer = []
    
    visited = [False]*len(tickets)
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
        
        
    dfs("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]

#뭐가 문제인지 모르겠다
