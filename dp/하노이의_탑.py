def solution(n):
    answer = [[]]
    dic = {}
    dic[1] = [[1,3]]

    for i in range(2, n+1):
        dic[i] = []
        #1차
        for j in dic[i-1]:
            now = []
            for k in j:
                ele = k
                if ele == 2:
                    ele = 3
                elif ele == 3:
                    ele = 2
                now.append(ele)
            dic[i].append(now)

        dic[i].append([1,3])
        #2차
        for j in range(len(dic[i])-2, -1, -1):
            now = []
            for k in range(1,-1,-1):
                ele = dic[i][j][k]
                if ele == 3:
                    ele = 1
                elif ele == 1:
                    ele = 3
                now.append(ele)
            dic[i].append(now)


    return dic[n]




def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans  # 2차원 배열을 반환해 주어야 합니다.