import sys
sys.setrecursionlimit(10**7)

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        a = 20
        b = 20
        c = 20
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    

    result = w(a,b,c)
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,result))



