result = 0

def add(num) :
	global result
	result += num
	return result

def sub(num) :
	global result
	result -= num
	return result

def mul(num) :
	global result
	result *= num
	return result

def div(num) :
	global result
	result /= num
	return result

def start() :
	print("-Calculator v1.0-")
	while 1	:
		global result
		if result == 0 : 
			result = int(input("주연산자(수)를 입력하세요."))
		else :
			print(result)
		unResult = result

		sign = input("부호를 입력하세요. ! 를 입력하면 종료합니다.")
		if sign == '!' :
			break
		try :
			num = int(input("피연산자(수)를 입력하세요."))
		except :
			print("입력이 잘못되었습니다.")

		if sign == '+' :
			add(num)
			print(unResult, " ", sign, " ", num, " = ", result) 

		elif sign == '-' :
			sub(num)
			print(unResult, " ", sign, " ", num, " = ", result) 

		elif sign == '*' or sign =='x' :
			mul(num)
			print(unResult, " ", sign, " ", num, " = ", result) 

		elif sign == '/' :
			if num == 0 :
				print("0으로 나눌 수 없습니다. 처음으로 돌아갑니다.")
			else : 
				div(num)
				print(unResult, " ", sign, " ", num, " = ", result)

		else :
			print("입력이 잘못되어 처음으로 돌아갑니다.")
start()

