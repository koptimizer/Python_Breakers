import math, time, random

# 1. calculator 클래스 만들기
class Calculator :

    value = 0

    def _init_(self) :
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# 2. MaxLimitCalculator 클래스 만들기
class MaxLimitCalculator(Calculator) :
   def add(self, val) :
       self.value += val
       if self.value > 100 : self.value = 100

cals = MaxLimitCalculator()
cals.add(50)
cals.add(60)

print(cals.value)

# 3. 다음 결과를 예측해 보자.
# all([1,2,abs(-3)-3]) -> [1,2.0] 이 되므로 거짓이다.
# chr(ord('a')) == 'a' -> chr과 ord는 역의 관계이므로 참이다.

# 4. 리스트 [1,-2,3,-5,8,-3]에서 음수 제거
print(list(filter(lambda x : x > 0, [1, -2, 3, -5, 8, -3]))) # list 뺴면 디개 신기한일 발생

# 5. 0xea를 10진수로 변경하기
print(int(0xea))

# 6. map과 lambda를 사용하여 [1,2,3,4]리스트의 각 요솟값에 3이 곱해진 리스트 마들기
print(list(map(lambda x : x*3,[1,2,3,4])))

# 7. 리스트의 최솟값, 최댓값의 합
def MaxMinPlus(a) :
    minValue = min(a)
    maxValue = max(a)
    return minValue + maxValue

list_a = [-8,2,7,5,-3,5,0,1]
print(MaxMinPlus(list_a))

# 8. 17 / 3 의 결과값을 소숫점 4자리까지만 반올림
resultValue = 17 / 3
print(round(resultValue, 4))

# 9 ~ 11 불가

# 12. time 모듈을 사용하여 "yyyy/MM/DD hh:mm:ss "현재 날짜와 시간을 출력
print(time.strftime('%Y/%m/%d %X', time.localtime(time.time())))

# 13.  로또 번호 생성
def lottoNumMaker():
    nums = []
    i = 0
    while len(nums) < 6 :
        num = random.randint(1, 45)
        if num not in nums :
            nums.append(num)
    return sorted(nums)

print(lottoNumMaker())

# 번외 복잡한 람다식
최 = print
삡 = "Hello world!"
뺩 = 1

삡 = lambda 삠 : 삠 if 삠 < 뺩 else 삡(삠-뺩)+삠


최(삡(삡(삡(삡(뺩)+삡(뺩))+뺩)))

#삡(1-1) +1 = 1 = 1!
#삡(2-1) +2 = 3 = 2!
#삡(3-1) +3 = 6 = 3!
#삡(4-1) +4 = 10 = 4!
#삡(5-1) +5 = 14 = 5!...
#삡()은 인자로 받은 것을 팩토리얼로 반환한다.

#print(삡(삡(삡(삡(1)+삡(1))+1)
#print(삡(삡(삡(2)+1)))
#print(삡(삡(4)))
#print(삡(10))
#print(55)