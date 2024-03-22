person ={"달러":1320, "엔":950, "위안":182}

money=[13,200,13]

a = (person["달러"]*money[0]+person["엔"]*money[1]+person["위안"]*money[2])

print("철수가 가지고 있는 돈의 원화 가치는", end=" ")
print(a,end=" ")
print("원 입니다.")
