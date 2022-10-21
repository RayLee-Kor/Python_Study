#01
x = int(input("정수를 입력하시오: "))
y = int(input("정수를 입력하시오: "))
if x%y == 0 :
    print("약수입니다.")

#02
x = int(input("정수를 입력하시오: "))
if x>25 :
    print("반바지를 추천합니다.")
else :
    print("긴바지를 추천합니다.")

#03
s = input("문자를 입력하시오: ")
if s == 'R' or s=='r':
print("Rectangle")
elif s == 'T' or s=='t':
print("Triangle")
elif s == 'C' or s=='c':
print("Circle")
else :
print("Unknown")

#04
x = int(input("원의 반지름 : "))
if x < 0 :
    print("잘못된 값입니다.")
else :
    print("원의 면적 : ", x*x*3.14)

#05
x, y, z = eval(input("3개의 정수를 입력하시오: "))
#eval은 좋지 않은 표현이다. 사실 split을 통해 배열로 만들 수 있지만 일단 eval을 쓰겠다.
if x > y :
    if y < z:
        print("제일 작은 정수는 ", y, "입니다.")
    else :
        print("제일 작은 정수는 ", z, "입니다.")
else:
    if x < z:
        print("제일 작은 정수는 ", x, "입니다.")
    else :
        print("제일 작은 정수는 ", z, "입니다.")
        
#06
import random
x=int(input("선택하시오(1: 가위 2: 바위 3: 보) "))
num=random.randint(1, 3)
print("컴퓨터의 선택 (1: 가위 2: 바위 3: 보) ",num)
if x == num :
    print("비겼음")
elif x == 1 :
    if num == 2:
        print("컴퓨터가 이겼음")
    elif num == 3 :
        print("당신이 이겼음")
elif x == 2 :
    if num == 3:
        print("컴퓨터가 이겼음")
    elif num == 1 :
        print("당신이 이겼음")
elif x == 3 :
    if num == 1:
        print("컴퓨터가 이겼음")
    elif num == 2 :
        print("당신이 이겼음")

#07
x=int(input("키를 입력하시오(cm) "))
y=int(input("나이를 입력하시오 : "))
if x >= 140 and y>=10 :
    print("타도 좋습니다")
else :
    print("죄송합니다")

#08
w, h = map(int, input("체중과 키를 입력하시오 :").split())
x=(h-100)*0.9
if w>x :
    print("과체중입니다.")
elif w<x:
    print("저체중입니다.")
else :
    print("표준입니다.")

#09
import random

x = random.randint(1, 10)
y = random.randint(1, 10)
op = random.randint(0, 4)

if op == 0 :
    answer = int(input(str(x) + " + " + str(y) + "의 값은?"))
    if x+y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
elif op == 1 :
    answer = int(input(str(x) + " - " + str(y) + "의 값은?"))
    if x-y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
elif op == 2 :
    answer = int(input(str(x) + " * " + str(y) + "의 값은?"))
    if x*y == answer:
        print("맞았습니다.")
    else: 
        print("틀렸습니다.")
else :
    answer = float(input(str(x) + " / " + str(y) + "의 값은?"))
    if x/y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

#10
x=float(input("x의 값을 입력하시오 : "))
if x>0:
    y=7*x+2
else :
    y=x**2-9*x+2
print("f(x)의 값은 ",y)

#11
weight = float(input("무게(킬로그램): "))
height = float(input("키(미터): "))

bmi = weight / height**2
print("당신의 BMI:", bmi)
if bmi >= 20.0 and bmi < 25.0 :
    print("정상입니다.")
elif bmi >= 25.0 and bmi < 30.0 :
    print("과체중입니다.")
elif bmi >= 30.0 :
    print("비만입니다.")

#12 원래 if문으로 해야되는데 일일이 하기 너무 귀찮아서 배열 사용
x=int(input("연도를 입력하시오: "))
number = x % 12
a=("원숭이띠","닭띠","개띠","돼지띠","쥐띠","소띠","호랑이띠","토끼띠","용띠","뱀띠","말띠","양띠")
print(a[number],"입니다.")

#13
year = int(input("연도를 입력하시오: "))
if (year % 4 == 0 and year%100 !=0) or year%400==0 :
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

#14
a = int(input("a를 입력하시오: "))
b = int(input("b를 입력하시오: "))
c = int(input("c를 입력하시오: "))
d = (b**2) - (4*a*c)
if d>0:
    r1= (-b + (b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print("실근은 {} 와 {} 입니다.".format(r1,r2))
elif d==0:
    x = -b / 2*a
    print("중근입니다. 해는 {}입니다.". format(x))
else:
    r1= (-b + (b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print("허근은 {} 와 {} 입니다.".format(r1,r2))

#15
num = int(input("정수를 입력하시오: "))
if num%3==0 and num%5==0: print('Python Express')
elif num%3==0: print('Python')
elif num%5==0: print('Express')

#16
x=float(input("pH를 입력하시오: "))
if(x==7.0) :
    print("중성입니다.")
elif(x>7.0) :
    print("알칼리입니다.")
else :
    print("산입니다.")
