def solution(n, times):
    answer = 0
    # 가능한 최댓 값과 최솟값을 left와 right로 설정
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            
            # 중간에 n 명 보다 많이 심사했다면
            if people >= n:
                break
        # 심사한 사람이 n보다 많다면 mid가 컸던 것
        if people >= n:
            answer = mid
            right = mid - 1
        # 아니라면 mid 가 작았던 것
        else:
            left = mid + 1
            
    return answer

# input 의 범위가 길고 특정 값을 찾아야 한다면 이분 탐색을 고민해본다
# 이분 탐색은 범위가 sort 되어 있어야 함