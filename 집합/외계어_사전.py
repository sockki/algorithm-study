def solution(spell, dic):
    answer = 2
    spell = set(spell)
    
    for i in dic:
        ans = set()
        for j in i:
            if j in spell:
                ans.add(j)
        if len(ans) < len(spell):
            continue
        else:
            answer = 1
            break
            
    
   
    return answer

    #집합 선언은 i = set()
    #집합은 자동으로 중복을 지운다
    #집합은 순서가 없다.