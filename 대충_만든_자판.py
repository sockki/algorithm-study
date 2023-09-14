def solution(keymap, targets):
    gil = len(keymap)
    dic = [{} for _ in range(gil)]
    index = 0
    answer = []
    for i in keymap:
        for j, v in enumerate(i):
            if v in dic[index]:
                continue
            dic[index][v] = j + 1
        index += 1

    result = 0
    results = []
    for target in targets:
        for moonja in target:
            for k in dic:
                if moonja in k:
                    results.append(k[moonja])

            if results:
                result += min(results)
                results = []
            else:
                result = -1
                break

        answer.append(result)
        result = 0

    return answer

# 반례를 잘 생각하자.
