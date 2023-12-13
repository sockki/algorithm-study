def maxdivisor(numb):
    if numb == 1:
        return 0
    ans = [1]
    for i in range(2, int(numb**(1/2)) + 1):
        if (numb % i == 0) and i <= 1e7:
            ans.append(i)
            if numb//i <= 1e7 and numb//i != numb:
                ans.append((numb // i))
        
    return max(ans)

def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        answer.append(maxdivisor(i))
    return answer

## for i in range(2, int(numb**(1/2)) + 1):
# 최대약수를 구할 때 필요한 알고리즘, 제발 기억하자