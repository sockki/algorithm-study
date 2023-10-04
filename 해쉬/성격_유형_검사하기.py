# 나의 풀이

def solution(survey, choices):
    TR = 0
    FC = 0
    MJ = 0
    NA = 0
    gile = len(survey)
    for i in range(gile):
        if survey[i].find("R") >= 0:
            if survey[i] == "RT":
                TR += score(choices[i], 1)
            else:
                TR += score(choices[i], 0)
        elif survey[i].find("C") >= 0:
            if survey[i] == "CF":
                FC += score(choices[i], 1)
            else:
                FC += score(choices[i], 0)
        elif survey[i].find("J") >= 0:
            if survey[i] == "JM":
                MJ += score(choices[i], 1)
            else:
                MJ += score(choices[i], 0)
        elif survey[i].find("A") >= 0:
            if survey[i] == "AN":
                NA += score(choices[i], 1)
            else:
                NA += score(choices[i], 0)
    answer = []

    if TR >= 0:
        answer.append("R")
    else:
        answer.append("T")
    if FC >= 0:
        answer.append("C")
    else:
        answer.append("F")
    if MJ >= 0:
        answer.append("J")
    else:
        answer.append("M")
    if NA >= 0:
        answer.append("A")
    else:
        answer.append("N")

    return ("".join(answer))


def score(choice, reverse):
    if reverse == 0:
        return (choice - 4)
    else:
        return (4-choice)

# 다른 사람 풀이


def solution(survey, choices):

    my_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for A, B in zip(survey, choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

# 보면 1단계만 그런 것 인지는 모르겠지만, 카카오는 매 문제마다 가장 효율적인 함수 사용이
# 우선인것 같다. for A,B in zip(... , ...) 를 잘 기억해보자
