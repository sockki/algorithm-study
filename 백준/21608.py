#1. 숫자 갯수만큼 graph 전체 for 문을 돈다.
#2. 돌다가 0 인 곳을 만나면 want 함수로 이동
#3. want에서는 0인 곳의 인접 4방향을 돌면서 좋아하는 학생이 있는 수와 빈자리의 수를 센다.
#4. 좋아 하는 학생의 수가 지금까지 for 문 돌면서 만난 0 인 곳 중에서 가장 높으면 
# hoo 배열을 초기화 하고 hoo에 [zerocount,yy,xx]를 append
# 똑같다면 hoo에 [zerocount,yy,xx] append
#5. 한차례의 for문이 끝나면 hoo 배열을 reverse sort 하여서 그중 첫번째 index의 저장된 값에 학생을 자리시킴
#6. 모든 for문 다 돌면 graph 돌면서 각 자리마다 인접 4방향을 돌면서 만족도를 센다.

import sys

dy = [1,0,-1,0]
dx = [0,-1,0,1]

def searchLike(y,x):
    global max,hoo
    likecount = 0
    zerocount = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0<=yy<n and 0<=xx<n:
            if graph[yy][xx] in student[count]:
                likecount += 1
            elif not graph[yy][xx]:
                zerocount += 1

    if likecount > max:
        max = likecount
        hoo = []
        hoo.append([zerocount,y,x])
    elif likecount == max:
        hoo.append([zerocount,y,x])


n = int(sys.stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
student = []
for i in range(n*n):
    student.append(list(map(int,sys.stdin.readline().split())))

count = 0
while count < n*n:
    hoo = []
    max = 0
    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                searchLike(i,j)

    hoo.sort(key=lambda x: (x[0], -x[1],-x[2]))
    a,b,c = hoo.pop()
    graph[b][c] = student[count][0]
    
    count += 1

result = 0
student.sort()
for i in range(n):
    for j in range(n):
        how = 0
        for l in range(4):
            ii = i + dy[l]
            jj = j + dx[l]
            if 0<=ii<n and 0<=jj<n and graph[ii][jj] in student[graph[i][j]-1]:
                how += 1
        if how == 0:
            result += 0
        else:
            result += 10**(how - 1)


print(result)

