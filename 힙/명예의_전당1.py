from heapq import *


def solution(k, score):
    hof = []
    answer = []
    count = 0
    for i in score:
        count += 1
        heappush(hof, i)

        if (count > k):
            heappop(hof)
        answer.append(hof[0])

    return answer

# heap 에서 제일 낮은 값은 [0] index에 저장이 된다.
