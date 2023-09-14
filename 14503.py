import sys

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def robot(r,c,bang):
    index = bang
    chase = True
    result = 1
    roboty = r
    robotx = c
    graph[roboty][robotx] = 2
    while chase:
        chase = False
        for i in range(4):
            index = (index + 1) % 4
            if(graph[roboty + dy[index]][robotx + dx[index]] == 0 and 0 <= roboty + dy[index] < n and 0 <= robotx + dx[index] < m):
                roboty = roboty + dy[index]
                robotx = robotx + dx[index]
                graph[roboty][robotx] = 2
                result += 1
                chase = True
                break

        
        if chase == False:
            if(graph[roboty + dy[(index + 2)%4]][robotx + dx[(index + 2)%4]] == 2):
                roboty = roboty + dy[(index + 2)%4]
                robotx = robotx + dx[(index + 2)%4]
                chase = True
            else:
                chase = False
            
                
    
    return result



graph = []
n,m = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

if d == 1:
    d = 3
elif d == 3:
    d = 1
    
ans = robot(r,c,d)
print(ans)