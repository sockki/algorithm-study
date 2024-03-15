-- 코드를 입력하세요
SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP,
COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP

'TRUNCATE(a,b) a는 나눌 숫자, b는 자릿수'
'0: 소수점 이하'
'-1: 1의 자리 이하'
'1: 소수점 1번째 자리 이하'
'TRUNCATE는 내림, ROUND는 반올림'