from heapq import *


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    mins = scoville[0]
    while mins < K and len(scoville) > 1:
        a = heappop(scoville)
        b = heappop(scoville)
        answer += 1
        heappush(scoville, a + b*2)
        mins = scoville[0]

    if mins < K:
        return -1

    return answer
