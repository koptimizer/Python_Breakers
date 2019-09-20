#헬로 월드 출력
print("hello world!")

#리스트 이해
squares = [1, 3, 5, 4, 8]
print(squares)

#피보나치 수열
a, b = 0, 1
while(a<100):
    print(a)
    b= a+b;
    a= b-a

#range()이해
print(range(10)) # else 의 반환객체는 list가 아닌 literable

# 소수 찾기
for n in range(0, 10000):
    if n == 0 or n == 1 :
        print(n, "은 소수가 아닙니다.")

    else :
        for m in range(2, n):
            if n % m == 0:
                print(n, ": ", m, "* ", n//m)
                break
        else : # for 리스트 소진 시 else로 감
            print(n, "은 소수입니다")



