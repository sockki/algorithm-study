import sys
import heapq

  

n = int(sys.stdin.readline())
gang = []
for i in range(n):
  a,b = map(int,sys.stdin.readline().split())
  heapq.heappush(gang, (b,a))


now = 0
cnt = 0
while gang:
  b,a = heapq.heappop(gang)
  if a >= now:
    now = b
    cnt += 1

print(cnt)

# heapq에 tuple이 삽입될 시에 tuple의 첫번째 원소를 기준으로 정렬이 된다.