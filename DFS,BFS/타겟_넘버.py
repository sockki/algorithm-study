def solution(numbers, target):
    answer = 0

    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
                return
            else:
                return

        result += numbers[idx]
        dfs(idx+1, result)
        result -= numbers[idx]
        result -= numbers[idx]
        dfs(idx+1, result)

    dfs(0, 0)

    return answer

# nonlocal은 부모 함수의 지역변수를 사용 할 수 있게 해줌
# global은 전역 변수를 사용 할 수 있게 해줌
