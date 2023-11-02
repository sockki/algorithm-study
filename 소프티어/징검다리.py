import sys

n = int(sys.stdin.readline())
dolls = list(map(int,sys.stdin.readline().split()))

result = [1] * n
for i in range(len(dolls)):
  result_max = 0
  for j in range(i):
    if dolls[i] > dolls[j]:
      if result[j] > result_max:
        result_max = result[j]
  result[i] = result_max + 1


print(max(result))
  
