#01
myList = [80,20,20,30,60,30]
myList = set(myList)
myList = list(myList)
myList.sort()
print(myList)

#02
a = {x:x**2 for x in range(1,11,1)}
print(a)

#03
d={"Apple":1,"Banana":2,"Grape":3}
for a, b in d.items() :
    print(a,"->",b)

#04
d={1:10,2:20,3:30,4:40,5:50,6:60}
x = int(input("키를 입력하시오 : "))
if x in d :
    print("키 ",x,"은 딕셔너리에 있습니다.")

#05
myDict = {"옷": 100, "컴퓨터": 2000, "모니터": 320}
print("총합계=", sum(myDict.values()))

#06
colors = ["red","green","blue"]
values = ["#FF0000", "#008000","#0000FF"]
print(dict(zip(colors,values)))

#07
mydict = {}

for i in range(2):
    date = input("날짜를 입력하시오: ")
    job = input("일정을 입력하시오: ")

    if date in mydict:
        mydict[date].append(job)
    else:
        mydict[date] = []
        mydict[date].append(job)
print(mydict)

#09
s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

set1=set(s1)
set2=set(s2)

print("모두 포함된 글자: ", set1 and set2)

#10
set1 = {10,20,30,40,50,60}
set2 = {30,40,50,60,70,80}
allset = set1 & set2
print(set1)
print(set2)
getset = set1-allset | set2-allset
print("어느 한쪽에만 있는 요소들 : ",getset)

#11
problems = {"파이썬": "최근에 가장 떠오르는 프로그래밍 언어",
             "변수": "데이터를 저장하는 메모리 공간",
             "함수": "작업을 수행하는 문장들의 집합에 이름을 붙인것",
             "리스트": "서로 관련이 없는 항목들의 모임",
             }

def show_words(problems):
    display_message = ""
    i=1
    for word in problems.keys():
        display_message += "("+str(i)+")"
        display_message += word + " "
        i+=1
    print( display_message)

for meaning in problems.values():
    print("다음은 어떤 단어에 대한 설명일까요? ")
    print("\""+meaning+"\"")
    correct = False
    while not correct:
        show_words(problems)
        guessed_word = input("")
        if problems[guessed_word] == meaning:
            print("정답입니다. !")
            correct = True
        else:
            print("정답이 아닙니다.")

#12
x = input("문자열 입력 : ")
y = input("금칙어 입력 : ")
x=x.replace(y,'****')
print(x)

#13
def count_all(txt):
    return {
        "LETTERS": sum(1 for x in txt if x.isalpha()),
        "DIGITS": sum(1 for x in txt if x.isnumeric()),
        }
print(count_all("Hello World123"))

#14
x="05/21/2020"
y="12/31/2020"
getx= x.split("/")
gety= y.split("/")
print(x," -> ", "".join(getx))
print(y," -> ", "".join(gety))

#15
studentList = {
"Park": "Korea",
"Sam": "USA",
"Sakura": "Japan"
}
def greeting(name):
    if name in studentList:
        return 'Hi! I"m ' + name+ ', and I"m from ' + studentList[name] + "."
    else:
        return 'Hi! I"m a guest.'
    
print(greeting("Park"))
print(greeting("Sam"))
print(greeting("Sakura"))