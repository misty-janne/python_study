# Chapter02-2_ex1.py
# 파이썬 완전 기초
# print 사용법

"""
참고: Escape 코드

\n: 개행
\t: 탭
\\: 문자
\': 문자
\": 문자
\000: 널 문자
'''
"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)
# n = Lee, s = 308276567, sum = 150

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)
# n = Lee, s = 308276567, sum = 150

# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)
# n = Lee, s = 308276567, sum = 150

print(f'n = {n}, s = {text}, sum = {x + y}')
# n = Lee, s = 308276567, sum = 150


# 구분기호
m = 10000000000
print(f'm : {m:,}')
# m : 10,000,000,000


# 정렬
# ^: 가운데, <: 왼쪽, >: 오른쪽

t = 20

print(f"t : {t:10}")
# t :         20

print(f"t center : {t:^10}")
# t center :    20

print(f"t left : {t:<10}")
# t left : 20

print(f"t right : {t:>10}")
# t right :         20


# 자릿수를 특정 문자열로 채우기

print(f"t center : {t:-^10}")
# t center : ----20----

print(f"t left : {t:#<10}")
# t left : 20########
