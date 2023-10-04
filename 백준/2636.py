#1. 매시간 마다 치즈가 녹기 전에 전체 칸을 for문 순회 할 것이다. 그리고 visit 문을 초기화
# 이때 순회할 때 1을 만나지 못하면 nonecheese는 true이고 while문이 끝난다.
#2. 칸이 비어 있고, visit 문 에서 들리지 않았다면 함수로 들어간다.
#3. 함수에서는 bfs를 할 것이고, 들리지 않은 빈칸을 찾을 것이다. 이때 그 빈칸을 찾을 때마다, 배열에 넣는다.
#4. 만약 빈칸을 bfs 순회를 하다가, 벽면을 만나면 hole = false 이다. 그리고 순회를 마치면 배열을 비운다.
#5. 벽면을 만나지 않는 경우에 hole = true 이며, 이때 빈칸 순회를 마치면 배열을 그대로 보존한다. 그리고 그 배열의 길이만큼
#pop 하여서 그 값들을 nowholes 배열에 append 한다.
#6. 다시 처음부터 순회를 하여서 치즈인 부분을 찾는다. 이때 치즈인 칸 중에서 빈칸의 좌표인 1과 닿아있고 그 칸이 nowhole에 있지 않다면
#그 치즈를 erasecheese 배열에 넣는다.
#7. 순회가 끝나면 그 배열을 길이만큼 pop 하여 좌표를 받아서 지우고 nowhole도 초기화 한다. 
# 이때 erasecheese의 길이를 보존한다. 이 사이클이 한시간이다.
#8. 1에서 nonecheese가 true 이면 while이 끝나고 사이클의 길이와 erasecheese를 출력

import sys
from collections import deque

dy = [1,0,-1,0]
dx = [0,-1,0,1]

def bfs(y,x):
    queue = deque()
    queue.append([y,x])
    zeros = []
    buck = False
    visit[y][x] = 1
    zeros.append([y,x])
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            yy = a + dy[i]
            xx = b + dx[i]
            if 0<=yy<se and 0<=xx<ga and not graph[yy][xx] and not visit[yy][xx]:
                queue.append([yy,xx])
                visit[yy][xx] = 1
                zeros.append([yy,xx])
                if yy == 0 or yy == (se - 1) or xx == 0 or xx == (ga - 1):
                    buck = True

    z = len(zeros)
    if buck == False:
        for i in range(z):
            c,d = zeros.pop()
            nowholes.append([c,d])




se,ga = map(int,sys.stdin.readline().split())
graph = []
for i in range(se):
    graph.append(list(map(int,sys.stdin.readline().split())))

noncheese = False
count = 0
e= 0

while not noncheese:
    visit = [[0 for _ in range(ga)] for _ in range(se)]
    nowholes = []
    erasecheese = []
    noncheese = True
    for i in range(se):
        for j in range(ga):
            if not graph[i][j] and not visit[i][j]:
                bfs(i,j)
            if graph[i][j]:
                noncheese = False

    if noncheese:
        break

    for i in range(se):
        for j in range(ga):
            if graph[i][j]:
                for l in range(4):
                    ii = i + dy[l]
                    jj = j + dx[l]
                    if not graph[ii][jj] and [ii,jj] not in nowholes:
                        erasecheese.append([i,j])
                        break
    e = len(erasecheese)
    for i in range(e):
        c,d = erasecheese.pop()
        graph[c][d] = 0

    count += 1
    

print(count)
print(e)


                    
