import sys
dy = [0,-1,-1,-1,0,1,1,1]
dx = [-1,-1,0,1,1,1,0,-1]
by = [1,1,-1,-1]
bx = [-1,1,-1,1]




n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = []
s = []
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    d.append(a)
    s.append(b)

cloud = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]
visit = [[0] * n for _ in range(n)]

for i in range(m):
    # 1. 이동시켜서 그 수가 n보다 커지면 1과 연결, 1보다 작아지면 n과 연결
    for j in range(len(cloud)):
        # 이거 계산하는거 알아두자
        cloud[j][0] = (cloud[j][0] + dy[d[i]-1]*s[i])%n
        cloud[j][1] = (cloud[j][1] + dx[d[i]-1]*s[i])%n
    # 2. 구름이 있는 칸 이면 물을 추가
    for k,l in cloud:
        graph[k][l] += 1
        visit[k][l] = 1
    
    # 4. 대각선을 봤을 때 경계를 안넘어가고 물이 있다면 count를 세고 그 수만큼 물을 추가
    for k,l in cloud:
        count = 0
        for p in range(4):
            kk = k + by[p]
            ll = l + bx[p]
            if 0 <= kk < n and 0 <= ll < n and graph[kk][ll]:
                count += 1
        graph[k][l] += count

    # 3.
    cloud = []    

    # 5. 구름이었던 칸이 아닌게 확인되고 물의 양이 2 이상이면 그 칸의 물의 양
    # -2 이후 cloud에 추가, visit로 1로 set
    # 구름이었던 칸인 경우 visit를 0으로 set
    for j in range(n):
        for k in range(n):
            if visit[j][k]:
                visit[j][k] = 0
            else:
                if graph[j][k] >= 2:
                    graph[j][k] -= 2
                    cloud.append([j,k])

result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

print(result)


        





