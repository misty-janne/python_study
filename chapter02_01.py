# Chapter02-1
# 파이썬 완전 기초
# print 사용법

print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

## 기본 개행 적용
print()

# separator 옵션

print('P', 'Y', 'T', 'H', 'O', 'N')
## 출력|P Y T H O N

print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
## 출력|PYTHON

print('P', 'Y', 'T', 'H', 'O', 'N', sep='   ')
## 출력|P   Y   T   H   O   N

print('010', '7777', '1234', sep='-')
## 출력|010-7777-1234

print('python', 'google.com', sep='@')
## 출력|python@google.com

# end 옵션

print('Welcome to', end='')
print('IT News', end='')
## 출력|Welcome toIT News

print()

# file 옵션

import sys
print('Learn Python', file=sys.stdout)

# format 사용(d: 3, s: 'python', f: 3.144545454)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
## 출력|one two

print('{1} {0}'.format('one', 'two'))
## 출력|two one

# %s

print('%10s' % 'nice', end='')
print('{:>10}'.format('nice'))
## 출력|      nice      nice

print('%-10s' % 'nice', end='')
print('{:10}'.format('nice'))
## 출력|nice      nice      

print('{:_>10}'.format('nice'))
## 출력|______nice

print('{:^10}'.format('nice'))
## 출력|   nice   

print('%.5s' % ('pythonstudy'))
## 출력|pytho

print('{:10.5}'.format('pythonstudy'))
## 출력|pytho     
## 10개의 공간에서 5개의 문자열 절삭하여 출력

# %d

print('%d %d' % (1,2))
print('{} {}'.format(1,2))
## 출력|1 2

print('%4d' % (42))
print('{:4d}'.format(42))
## 출력|  42

print('%4d' % (4564354353))
## 출력|4564354353

# %f

print('%f' % (3.1455435435565435))
print('{:f}'.format(3.1455435435565435))
## 출력|3.145544

print('%1.8f' % (3.1455435435565435))
## 출력|3.14554354
## 정수부 1자리, 소수부 8자리

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
## 출력|003.14
## 총자릿수 6자리, 정수부 1자리이므로 공백을 0으로 채움, 소수부 2자리


