from collections import deque
def solution(data, col, row_begin, row_end):
    answer = 0
    S_i_arr = []
    data.sort(key = lambda x : [x[col-1], -x[0]])
    for i in range(row_begin, row_end + 1):
        S_i = 0
        for j in data[i-1]:
            S_i += int(j % i)
        S_i_arr.append(S_i)
    
    S_i_arr = deque(S_i_arr)
    now = 0
    while S_i_arr:
        now = S_i_arr.popleft()
        answer = answer ^ now
    return answer