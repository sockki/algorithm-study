def solution(board, skill):
    answer = 0
    w = len(board[0])
    h = len(board)
    new = [[0 for i in range(w + 1)] for i in range(h + 1)]
    for s in skill:
        if s[0] == 1:
            new[s[1]][s[2]] -= s[5]
            new[s[3]+1][s[4]+1] -= s[5]
            new[s[1]][s[4]+1] += s[5]
            new[s[3]+1][s[2]] += s[5]
        else:
            new[s[1]][s[2]] += s[5]
            new[s[3]+1][s[4]+1] += s[5]
            new[s[1]][s[4]+1] -= s[5]
            new[s[3]+1][s[2]] -= s[5]
            
    for i in range(1,w+1):
        for j in range(h+1):
            new[j][i] += new[j][i-1]
    
    for j in range(1,h+1):
        for i in range(w+1):
            new[j][i] += new[j-1][i]
            
    for i in range(h):
        for j in range(w):
            if board[i][j] + new[i][j] > 0:
                answer += 1
    return answer

# 그래프 순회에서 시간초과가 나면 누적합을 생각해보자