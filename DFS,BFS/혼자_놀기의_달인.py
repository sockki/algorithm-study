def solution(cards):
    answer = []
    result = []
    boxOpen = [0 for i in range(len(cards))]
    def dfs(cards, n, answers):
        nonlocal boxOpen, result
        
        if boxOpen[n-1] == 1:
            result.append(answers)
        else:
            boxOpen[n-1] = 1
            answers.append(cards[n-1])
            dfs(cards, cards[n-1], answers)
    
    for i in range(len(boxOpen)):
        if boxOpen[i] == 0:
            answers = []
            dfs(cards,i+1, answers)
            
    if len(result) == 1:
        return 0
    else:
        for i in result:
            answer.append(len(i))
        answer.sort(reverse=True)
            
            
    
    return answer[0] * answer[1]
