
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