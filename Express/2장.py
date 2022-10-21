#01
x = int(input("x: "))
y = int(input("y: "))
 
print("두수의 합: ", x+y)
print("두수의 차: ", x-y)
print("두수의 곱: ", x*y)
print("두수의 평균: ", (x+y)/2)
print("큰수: ", max(x, y))
print("작은수: ", min(x, y))

#02
chicken = 2
pig = 4
cow = 3
leg = chicken * 2 + pig * 4 + cow * 4
print("닭의 수 : ", chicken)
print("돼지의 수 : ", pig)
print("소의 수 : ", cow)
print("전체 다리의 수 : ", leg)

#03
x = int(input("삼각형의 첫번째 변의 길이 : "))
y = int(input("삼각형의 두번째 변의 길이 : "))
print("삼각형의 나머지 변의 최대 길이 : ", int(x+y)-1)

#04
x = int(input("시간을 입력하시오 : "))
y = int(input("분을 입력하시오 : "))
print(x," 시간",y," 분은", 60*60*x+60*y," 초입니다")

#05
x = int(input("화씨 온도를 입력하시오 : "))
tem = (float(x)-32.0)*5/9
print("화씨 ", x,"도는 섭씨 ",round(tem,2),"도에 해당합니다.")

#06
x = int(input("음식 비용 : "))
print("팁 비율 : 10%")
print("총액 : ",round(x*1.1),"달러")

#07
x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
dist = ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
print("두점 사이의 거리 = ",dist)

#08, 07계산과 동일
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.left(45)
t.forward(141)
t.back(141)
t.right(45)
t.forward(100)
t.left(90)
t.forward(100)

#09
n = int(input("정수="))
s = 0
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
print(s)


#10
import turtle
t = turtle.Turtle()
t.shape("turtle")
side = 100
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)

#11
x = input("드라이브 이름 : ")
y = input("디렉토리 이름 : ")
z = input("파일 이름 : ")
a = input("확장자 : ")
print("완전한 이름은 ", x+":"+y+z+"."+a)

#12
x = int(input("숫자를 입력하시오 : "))
print(format(x, ',d'))