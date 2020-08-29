def prac1():
    while 1:
        ident = ""
        identOk = 0
        identResult1 = ""
        identResult2 = ""

        ident = input("주민번호를 -를 포함하여 입력하여주세요.")
        # 하이픈이 한개만 포함되어 있는지 검사. 합격시 identOk 에 +1
        for item in ident :
            if item == '-' :
                identOk +=1

        # 총 입력받은 문자가 14자리 인지 검사. 합격시 identOk 에 +1
        if len(ident) == 14 :
            identOk +=1
        else :
            print("주민번호를 다시 입력하세욥!")

        # identOk변수가 2일 경우 모든 조건을 합격 했으므로 스트링 분리 시작
        if identOk == 2 :
            identResult1 = ident[:6]
            identResult2 = ident[7:]
            print(identResult1, identResult2)
        else :
            print("다시 입력해주세요.")

def prac2():
    while 1:
        ident = ""
        identOk = 0
        gender = ""

        ident = input("주민번호를 -를 포함하여 입력하여주세요.")
        # 하이픈이 적절히 포함되어 있는지 검사. 합격시 identOk 에 +1
        for item in ident :
            if item == '-' :
                identOk +=1
        if identOk == 1 and ident[6] == "-" :

            # 총 입력받은 문자가 14자리 인지 검사. 합격시 identOk 에 +1
            if len(ident) == 14 :
                identOk +=1

                # identOk변수가 2일 경우 모든 조건을 합격 했으므로 스트링 인덱싱 시작
                # 주민번호 7번째 자리가 성별을 구분하는 자리이므로, 그 숫자에 따라 남녀 구별
                if identOk == 2 :
                    gender = int(ident[7])
                    if gender == 1 or gender == 3 :
                        print("남자")
                    elif gender == 2 or gender == 4 :
                        print("여자")
                    else :
                        print("잘못된 주민번호입니다. 주민번호를 다시 입력해주세요.")
            else:
                print("14자리 주민번호를 입력해주세요.")
        else :
            print("하이픈을 포함해주시거나 한개만 포함해주세요!")

def prac3():
    while 1:
        tagString = ""
        testOk = 0
        result = ""
        firstTag = 0
        lastTag = 0
        tagString = input("tag로 둘러쌓인 문자열을 넣어주세요.")

        # 입력받은 문자열이 "<"로 시작하고 ">"로 끝나면 태그로 둘러쌓였다고 볼 수 있음.
        if tagString[0] == "<" and tagString[-1] == ">" :
            testOk +=1

        # 입력받은 문자열이 "<" 두개와 ">" 두개가 포함되었다면 적절한 태그로 둘러쌓였다고 볼 수 있음.
        for item in tagString :
            if item == "<" :
                firstTag +=1
            elif item == ">" :
                lastTag +=1
        if firstTag == 2 and lastTag ==2 :
            testOk +=1

        # testOk변수가 2일 경우 조건을 합격 했으므로 스트링 분리 시작
        if testOk == 2 :
            result = tagString.split(">")[1].split("<")[0].strip()
            print(result)
        else :
            print("잘못 된 형식의 스트링입니다.")

def prac4():
    while 1 :
        nolist = ""
        testOk = 0
        lists = ""
        sets = ""
        ascLists = []
        nolist = input("리스트의 요소를 ,로 구분해서 넣어주세요.")

        # 콤마로 구분했는지 검사
        for item in nolist :
            if item == "," :
                testOk +=1
                break

        # 맨 끝자리에 콤마가 들어가면 삭제
        if nolist[-1] == "," :
            nolist[-1] == ""

        # 콤마 구분이 되었다면(testOk==1) 콤마 단위로 잘라서 리스트로 집어 넣기
        if testOk == 1 :
            lists = nolist.split(",")

            # set()으로 중복 제거
            sets = set(lists)
            lists = list(sets)

            # 리스트의 요소를 ascii로 변환해서 다른 리스트에 저장
            try :
                for item in lists :
                    ascLists.append(ord(item))

                # ascii로 치환된 상태에서 정렬하고 목표 리스트를 초기화
                ascLists.sort()
                lists = []

                # 목표 리스트에 ascii로 변환된 리스트를 차례대로 받아오면서 아스키에 맞는 문자를 반환
                for item in ascLists :
                    lists.append(chr(item))

                print(lists)

            except :
                print("올바르지 않은 리스트 형식입니다. 요소에는 한자리의 문자만 허용됩니다.")
        else :
            print("올바르지 않은 리스트 형식입니다.")

def prac5() :
    while 1 :
        sent = ""
        result = ""
        sent = input("문장을 입력해주세요!")

        result = sent.split(" ")
        print(result)