def solution(name, yearning, photos):
    answer = []
    dic = {}
    for a,b in zip(name,yearning):
        dic[a] = b
    for photo in photos:
        result = 0
        for p in photo:
            if p in dic:
                result += dic[p]
        answer.append(result)
    return answer

# dic에서 확인 할 때는 for dic[p] 가 아니라 for p in photo: