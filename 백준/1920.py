N = input()
N = int(N)
A = list(map(int, input().split()))
M = input()
M = int(M)
Mlist = list(map(int, input().split()))
count = 0

A.sort()

while count  < M:
    target = Mlist[count]
    count += 1

    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (high + low)/2
        mid = round(mid)
        if target == A[mid]:
            print(1)
            break
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if low > high:
            print(0)
            break

       