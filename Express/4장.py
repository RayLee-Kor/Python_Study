#01
for i in range(2, 51):
    if i%2==0 :
        print(i, end=" ")

#02
myList = [11,22,33,99,81,93,35]
sum = 0;
for i in myList :
    sum += i;
print("정수들의 합은 ", sum)

#03
sum=0
for i in range(1, 101):
    if i%3==0 :
        sum += i
print(sum)

#04
x = int(input("정수를 입력하시오 : "))
myList = []
for i in range(1,x+1) :
    if x % i == 0 :
        myList.append(i)
        i=i+1
    else :
        i=i+1
print("약수: ",end=" ")
for a in myList :
    print(a,end = " ")
  
#05
n = int(input("정수를 입력하시오: "))
for k in range(1, n+1):
    for i in range(1, k+1):
        print(i, end=" ")
    print()

#06
import math
print("각도 sin값 cos값")
for i in range(0,91,10) :
    print(i,"    ",round(math.sin(3.14*i/180.0),3),"    ",round(math.cos(3.14*i/180.0),3))

#07
import turtle
import math
t= turtle.Turtle()
t.shape("turtle")

for x in range(0, 360):
    t.goto(x,200*math.sin(x*3.14/180))

#08
n=1
while(n**2<=500) :
    n = n+1
print(n)

#09
for i in range (1,10) :
    for j in range(1,10) :
        print(i*j,end = " ")
        if j==9 :
            print(" ")

#10
sum=0
x = int(input("n의 값을 입력하시오 :"))
for a in range(x+1) :
    sum = sum + a**2
print("계산값은 ",sum,"입니다")

#11
x = int(input("첫번째 정수를 입력하시오: "))
y = int(input("첫번째 정수를 입력하시오: "))

m = min(x, y)

for x in range(1, m+1):
    if x%m==0 and y%m==0:
        gcd = m;
print("최대공약수=", gcd)

#12 몬테카를로 뭐 이상한거여서 안풀겠습니다
#13
nterms = int(input("몇 번째 항까지 구할까요? "))

n1, n2 = 0, 1
count = 0

while count <= nterms:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

#14
N = int(input()) # N=33 : 1~33중 소수인 것을 찾기. input()은 string이므로 int로 바꿔주어야 한다.
n=0 #찾은 소수의 개수를 알기위한 것
 
print(" 1부터 {}까지 소수 - ".format(N), end = ' ')
 
for i in range(2, N+1): #1은 당연히 소수가 아니므로 2부터 검사를 한다. 2 ~ N까지
    boolean = True # 처음에 모든 숫자를 소수라고 해놓고, 검사를해보자.
    for k in range(2, i): #자기자신(i)를 제외한다. 2 ~ i-1까지 반복
        if i%k == 0: #자기자신(i)전까지 나눴을 때, 나누어 떨어진다면,
            boolean = False # 소수가 아니다 -> false -> break : 더이상검사필요없음
            break
    if boolean is True: # boolean이 True 상태로 내려오면 소수라는 뜻이므로, 출력
        print(i, end= ' ') # enter가 아니라 바로 옆에 출력하기위한 것이다.
        n+=1 # 소수를 찾을 때마다 1씩 +하는 것이다.
 
print("\n 1부터 {}까지의 소수의 개수는 : {} 이다.".format(N,n))

#15
a=0
for i in range (1,100,2) :
    a=a+(i/(i+2))
print(a)

#16
x = int(input("게임판의 크기 : "))
for k in range (x) :
    for a in range(x) :
        print(" --- ", end = " ")
    print()
    for b in range(x+1) :
        print("|   ", end = " ")
    print()
for a in range(x) :
    print(" --- ", end = " ") # 마무리해주는 용도
    
#17
for i in range(10):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print('*')