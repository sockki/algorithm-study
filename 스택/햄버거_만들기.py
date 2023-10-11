def solution(ingredient):
    answer = 0
    need = []
    for i in ingredient:
        need.append(i)
        if need[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                need.pop()

    return answer
