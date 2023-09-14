import sys

N, M = map(int,sys.stdin.readline().split())


first = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
second = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
count = 0

if(N >= 3 and M >= 3):
    for i in range(N - 2):
       for j in range(M - 2):
            if first[i][j] != second[i][j]:
                count = count + 1
                for a in range(i,i + 3):
                    for b in range(j, j + 3):
                        first[a][b] = first[a][b] ^ 1
                    

for i in range(N):
    for j in range(M):
        if first[i][j] != second[i][j]:
            count = -1
            break
    
print(count)

