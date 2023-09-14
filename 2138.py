import sys

def switch(A,B):
    L = A[:]
    p = 0
    for i in range(1,n):
        if L[i-1] == B[i-1]:
            continue
        else:
            p += 1
            for j in range(i-1,i+2):
                if j < n:
                    L[j] = 1 - L[j]
    return p if L == B else 1e9





n = int(sys.stdin.readline())
first = list(map(int,input()))
second = list(map(int,input()))

result = switch(first, second)
first[0] = 1 - first[0]
first[1] = 1 - first[1]
result = min(result, switch(first,second) + 1)
print(result if result != 1e9 else -1)