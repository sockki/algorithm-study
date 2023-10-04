def solution(phone_book):
    l = len(phone_book)
    phone_book_set = set(phone_book)

    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in phone_book_set:
                return False

    return True


# list에서 in 연산은 O(n)시간이다. 마지막 인덱스 까지 찾으면 선형적으로 찾으므로 n 번 찾기 때문
# set과 dictionary에서 in 연산은 O(1)이다. 함수와 해시 테이블을 사용해서 만든 구조이므로 선형적으로 탐색하지 않기 때문
