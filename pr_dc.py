
#list 자료구조

praclist = ['apple', 'banana', 'carrot', 'danger', 'elephant' ]
praclist.append('fukuoka')
praclist.insert(6, 'guild')
praclist.remove('apple')
print(praclist.pop()) # 선입후출

print(praclist)

# stack list
stack = [3, 5, 7, 8]
stack.append(11)
stack.append(24)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

# que list
from collections import deque
que = deque([3, 5, 7, 9, 11])
que.append(23)
que.append(25)
que.popleft()
print(que)

# 리스트 컴프리헨션
squares_t = []
for x in range(10) :
    squares_t.append(x**2)
print(squares_t)

squares_t.clear()
squares_t = [x**2 for x in range(10)]
print(squares_t)

comb = [(x,y) for x in [1,7,9] for y in [1,9] if x != y]
print(comb)

# 리스트 컴프리헨션 -> 행열전치... 너무 신기하다
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)

# 튜플
t = 1234, 54321, "hello!"
print(t)

# 집합
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b) #차집합
print(a|b) #합집합
print(a&b) #교집합
print(a^b) #대칭차집합

c = {x for x in 'abracadabra' if x not in 'abc'} #리스트컴프리핸션 차집합
print(c)

# 딕셔너리(맵)
tel = {'jack' : 4098, 'sape' : 1494}
tel['gudo'] = 4127
print(tel)
# print(tel[0]) 배열로는 못부르넹
print(tel['jack'])
list(tel)
sorted(tel)
del(tel['jack'])
print(tel)
dicx = {x : x**2 for x in (2, 4, 6, 8)} # 딕셔너리 컴프리핸션
print(dicx)
print(dict(ape=133, wnw=1334, wkn=24)) # 키가 간단한 문자열이면 이렇게도 가능

#루프 테크닉
for i, w in tel.items():
    print(i,'+',w)
for i, w in enumerate(['tic', 'tac', 'toc']):
    print(i,w)

questions = ['name', 'birth', 'address', 'age']
answers = ['pang', '0710', '16030','23']

for q, a in zip(questions, answers):
    print("what is your {0}? It is {1}.".format(q, a))