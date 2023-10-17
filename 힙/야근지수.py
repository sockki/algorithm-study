import heapq

def solution(n, works):
    answer = 0
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    while n != 0:
        a = heapq.heappop(works)
        a += 1
        n -= 1
        heapq.heappush(works, a)
        
    answer = sum([w ** 2 for w in works])
    return answer

#[ i for i in arr ]
# 한즐 for 문을 잘 사용하자

# y = x**2 함수에 의해서 제일 큰 값부터 깎아나가면서 계산해야 한다.