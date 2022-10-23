#01
def get_peri(radius = 5.0):
    p = 2.0*3.141692* radius
    return p

print(get_peri()) # 기본 인수 사용
print(get_peri(4.0))

#02
x = int(input("첫번째 정수 입력 : "))
y = int(input("두번째 정수 입력 : "))
def get_x(x,y) :
    print(x,"+",y," = ", x+y)
    print(x,"-",y," = ", x-y)
    print(x,"*",y," = ", x*y)
    print(x,"/",y," = ", x/y)
get_x(x,y)

#03
def calc(a, b):
    return a+b, a-b, a*b, a/b

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("첫 번째 정수를 입력하시오: "))
a,b,c,d = calc(x, y)
print(a, b, c, d, "가 반환되었습니다")

#04
def getGrade(score) :
    if(score >= 90) :
        return 'A'
    elif score >= 80 :
        return 'B'
    elif score >= 70 :
        return 'C'
    elif score >= 60 :
        return 'D'
    else :
        return 'F'
x = int(input("점수를 입력하세요 : "))
print(getGrade(x))

#05
def checkpassword(s):
    digit, lower, upper = 0, 0, 0
    for i in s:
        if i.isupper():
            upper = 1
        elif i.islower():
            lower = 1
        elif i.isdigit():
            digit = 1
    if upper and lower and digit: print("사용할 수 있습니다.")
    else: print("사용할 수 없습니다.")

x= input("패스 워드를 입력하시오 : ")  
checkpassword(x)

#06
def getNumber(x,y) :
    print(x,"+",y,"의 합은?")
a = input("첫 번째 정수 입력 : ")
b = input("두 번째 정수 입력 : ")
getNumber(a,b)

#07
def getIntRange(a,b) :
    print("입력된 날짜는 ",a,"월 ",b,"일 입니다")
print("날짜를 입력하시오 (월과 일)")
while (True) :
    x = int(input("월을 입력(1부터 12사이) : "))
    if x >= 1 and x <= 12 :
        break
while (True) :
    y = int(input("일을 입력(1부터 31사이) : "))
    if y >= 1 and y <= 31 :
        break
getIntRange(x,y)

#07 다른 방식
def getIntRange(a, b, msg):
    x =-100
    while x < a or x > b:
        x = int(input(msg))
    return x

m = getIntRange(1, 12, "월을 입력하시오(1부터 12사이의 값): ")
d = getIntRange(1, 31, "일을 입력하시오(1부터 31사이의 값): ")
print(f"입력된 날짜는 {m}월 {d}일입니다.")

#08
def readNumber(n):
    units = ["","십","백","천"]
    nums = '일이삼사오육칠팔구'
    result = []
    i = 0
    while n>0:
        n,r = divmod(n,10)
        if r>0:
            result.append(nums[r-1]+units[i])
        i+= 1
    return "".join(result[::-1])

x = int(input("1000이하의 금액을 입력하시오 : "))
print(readNumber(x))

#09
def getGCD(a, b):
    gcd = 1
    i = 2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd = i
        i = i + 1
    return gcd
x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
print(getGCD(x, y))

#10
N=100
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

#11
def deci2bin(n):
    binary = ""
    while n != 0:
        value = n % 2
        if value == 0 :
            binary = "0" + binary
        else:
            binary = "1" + binary
        n = n // 2

    return binary
x = int(input("10진수: "))
print(deci2bin(x))

#12
def getSorted(x,y) :
    if x > y :
        a = x
        x = y
        y = a
    return x, y
a = int(input("첫번째 정수 : "))
b = int(input("두번째 정수 : "))
print(getSorted(a,b))
'''
#13
'''
import random

def dice_game() :
    human = random.randint(1,6)
    print("인간: 주사위값=", human )
    ai = random.randint(1,6)
    print("컴퓨터: 주사위값=", ai )
    if human > ai :
        print("인간승리")
    else:
        print("컴퓨터승리")
def main() :
    while True:
        dice_game()
        user = input("중단할까요? Y/N")
        if user == "Y" or user == "y":
            break;
main()