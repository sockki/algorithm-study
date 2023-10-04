from collections import Counter
import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()
san = round(sum(data)/n)
zoung = data[int((n-1)/2)]
binC = Counter(data).most_common()
if len(data) > 1 and binC[0][1] == binC[1][1]:
    bin = binC[1][0]
else:
    bin = binC[0][0]
bum = data[-1] - data[0]

print(san)
print(zoung)
print(bin)
print(bum)
