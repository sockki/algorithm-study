# 나의 풀이

def solution(today, terms, privacies):
    terms1 = []
    terms2 = []
    todaynum = []
    todaynum.append(int(today[0:4]))
    todaynum.append(int(today[5:7]))
    todaynum.append(int(today[8:]))

    for i in terms:
        terms1.append(i[0])
        terms2.append(int(i[2:]))

    gile = len(terms)
    index = 1
    answer = []

    for i in privacies:
        nowterm = i[11]

        for j in range(gile):
            years = 0
            month = 0
            days = 0
            if nowterm == terms1[j]:
                years = int(i[0:4])
                month = int(i[5:7]) + terms2[j]
                days = int(i[8:10])
                if month > 12:
                    years += month // 12
                    month = month % 12
                    if month == 0:
                        month = 12
                        years -= 1

                if todaynum[0] > years:
                    answer.append(index)
                elif todaynum[0] == years and todaynum[1] > month:
                    answer.append(index)
                elif todaynum[0] == years and todaynum[1] == month and todaynum[2] >= days:
                    answer.append(index)

        index += 1

    return answer

# 다른 사람 풀이


def solution(today, terms, privacies):
    answer = []
    termdict = {}

    for term in terms:
        t = term.split(' ')
        termdict[t[0]] = int(t[1]) * 28

    t = today.split('.')
    d = 28 * 12 * int(t[0]) + 28 * int(t[1]) + int(t[2])

    for p in range(len(privacies)):
        pret = privacies[p].split(' ')
        t = pret[0].split('.')
        nd = 28 * 12 * int(t[0]) + 28 * int(t[1]) + int(t[2])

        if termdict[pret[1]] + nd <= d:
            answer.append(p + 1)

    return answer

# 날짜 또는 시간 계산시에 아얘 전부 다 낮은 단위로 풀어서 계산하는 것이 정확할 것 같다.
# split함수를 사용해 보자
