def solution(n, k, enemy):
    answer = 0
    dp = [[0 for _ in range(len(enemy) + 1)] for _ in range(k + 2)]
    dp[1][0] = n
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1] - enemy[j-1])
            if j >= k and dp[i][j] == 0:
                print(i,j)
                answer = j - 1
                break
    return answer

print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))