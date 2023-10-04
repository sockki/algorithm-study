N,K = input().split()
N = int(N)
K = int(K)
count = 0

while bin(N).count('1') > K:
    count += 1
    N += 1

print(count)




