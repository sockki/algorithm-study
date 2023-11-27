def solution(numbers, hand):
    answer = ''
    btn = {1:[0,0], 2:[0,1], 3:[0,2],4:[1,0], 5:[1,1], 6:[1,2],7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    leftumm = [3,0]
    rightumm = [3,2]
    for i in numbers:
        if i in [1,4,7]:
            leftumm = btn[i]
            answer += "L"
        elif i in [3,6,9]:
            rightumm = btn[i]
            answer += "R"
        else:
            if (abs(btn[i][0] - leftumm[0]) + abs(btn[i][1] - leftumm[1])) < (abs(btn[i][0] - rightumm[0]) + abs(btn[i][1] - rightumm[1])):
                leftumm = btn[i]
                answer += "L"
            elif (abs(btn[i][0] - leftumm[0]) + abs(btn[i][1] - leftumm[1])) > (abs(btn[i][0] - rightumm[0]) + abs(btn[i][1] - rightumm[1])):
                rightumm = btn[i]
                answer += "R"
            else:
                if hand == "right":
                    rightumm = btn[i]
                    answer += "R"
                else:
                    leftumm = btn[i]
                    answer += "L"
            
    return answer