def solution(N, number):
    if number == 1:
        return 1
    set_list = []
    for cnt in range(1, 9):
        partial_set = set()
        partial_set.add(int(str(N) * cnt))
        for i in range(cnt - 1): 
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
        
    return -1

# dp를 풀때는 갯수를 먼저 생각한다.
#1. 탑다운(하향식, 메모이제이션 사용. 위=>아래)
#2. 보텀업(상향식. 아래=>위) 두 가지로 구성된다.
