import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

ab = [0 for _ in range(len(b))]
ans = 0

for i in range(len(a)):
    pre = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            ab[j] = pre + 1
        else:
            ab[j] = 0
        pre = ab[j]
    ans = max(ans,max(ab))


print(ans)

        