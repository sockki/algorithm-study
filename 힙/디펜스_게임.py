from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    answer = -1
    for i,v in enumerate(enemy):
        heappush(h,-v)
        n -= v
        if n < 0:
            if k > 0:
                k -= 1
                a = -heappop(h)
                n += a
                answer = i + 1
            else:
                answer = i
                break
        else:
            answer = i + 1

    return answer

# heappush, heappop원리를 잘 외우자. heappop은 가장 작은 원소 반환