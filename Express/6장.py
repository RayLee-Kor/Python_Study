#01
n = int(input("입력할 값의 개수: "))
result = [ ]

for i in range(n):
    value = int(input(""))
    result.append(value)
    
s = sum(result)
print("값의 합계=", s)

#02
import random
result = []
for i in range(10) :
    value = random.randint(1,100)
    result.append(value)

print(result)

#03
numbers = [20, 1, 12, 9, 18]

for value in numbers:
    print(value, "\t", "*" *  value)

#04
result = [-x if x>=3 and x<=8
          else x for x in range(1,11) ]
print(result)

#05
def match_words(words):
    x = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            x += 1
    return x

s= ['aba', 'xyz', 'abc', '121']
print(s)
print('문자열의 개수=', match_words(s))

#06
isOne = False
list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]
print(list1)
print(list2)
for i in list1 :
    for j in list2:
        if i == j:
            isOne = True
print(isOne)

#07
import random
list1 = ["a"+str(i) for i in range(10)]
print("list1=", list1)
print(random.choice(list1))

#08
a=[1,2,3,4,5]
b=[1,3,3,4,5,6,7]
result =[ x for x in a if x in b]
print(a)
print(b)
print(result)

#12
a=[[['#' for col in range(4)] for row in range(3)] for depth in range(2)]
print(a)

#13
seats = []
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])
seats.append([0,0,0,0,0,0,0,0,0,0])

def displayBookings():
    print("======================================")
    print("0 1 2 3 4 5 6 7 8 9 10")
    print("======================================")
    for row in seats:
        print(row)
    print("")
    
def reserv():
    row = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 –1)"))
    column = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 –1)"))
    if seats[row][column]==1:
        print("이미 예약된 자리입니다.")
    else:
        print("예약합니다.")
    seats[row][column]=1

displayBookings()
reserv()
displayBookings()