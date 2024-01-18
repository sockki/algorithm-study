def solution(orders):
    answer = 0
    nowcontainer = 1
    sidecontainer = []
    for order in orders:
        if order > nowcontainer:
            while order > nowcontainer:
                sidecontainer.append(nowcontainer)
                nowcontainer += 1
            nowcontainer += 1
            answer += 1

        elif order < nowcontainer:
            if sidecontainer[-1] == order:
                sidecontainer.pop()
                answer += 1
            else:
                break

        else:
            nowcontainer += 1
            answer += 1


    return answer