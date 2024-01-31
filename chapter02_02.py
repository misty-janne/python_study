# Chapter02-2.py
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
"700"
print(type(n))
"<class 'int'>"

# 동시 선언
x = y = z = 700
print(x, y, z)
"700 700 700"

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
"Change Value"
print(type(var))
"<class 'str'>"

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
"300"

# 예2)
# n -> 777
n = 777
print(n, type(n))
"777 <class 'int'>"

m = n
print(m, n)
"777 777"
print(type(m), type(n))
"<class 'int'> <class 'int'>"

m = 400
print(m, n)
"400 777"
print(type(m), type(n))
"<class 'int'> <class 'int'>"


# id(identity 확인): 객체의 고유값 확인

m = 800
n = 655

print(id(m))
"3041859338960"
print(id(n))
"3041859339056"
print(id(m) == id(n))
"False"

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
"1396423131856"
print(id(n))
"1396423131856"
print(id(m) == id(n))
"True"


# 다양한 변수 선언

# Camel Caes: numberOfCollegeGraduates -> Method
# Pascal Case: NumberOfCollegeGraduates -> Class
# Snake Case: number_of_college_graduates


# 허용하는 변수 선언 법

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age = 7
_AGE_ = 8


# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""
