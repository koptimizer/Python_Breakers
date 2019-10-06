from Scripts import mod as f
import sys

f.fib(1000)
print(f.fib2(100))
print(f.__name__)

from Scripts.mod import fib as fibo

fibo(500)

#모듈 정의 이름 찾기
print(dir(f))
print(dir(sys))
# 인자 없으면 현재 정의한 이름들 모두 나열
print(dir())


