# 8장
#01
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    
missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print (missy.getName(), missy.getAge())
print (lucky.getName(), lucky.getAge())

#02
class Rocket :
    def __init__(self,x,y) :
        self.x = x
        self.y = y

    def __str__(self) :
        return str(self.y)
    
    def moveUp(self) :
        self.y += 1


myRocket = Rocket(0,0)
print("높이 : ", myRocket.y)

myRocket.moveUp()
print("높이 : ", myRocket.y)

#03
class Box():
    def __init__(self, l, h, d):
        self.length=l
        self.height=h
        self.depth=d

    def __str__(self):
        return "("+str(self.length)+","+str(self.height)+","+str(self.depth)+")"

    def getLength(self):
        return self.length

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

b1 = Box(100, 100, 100)
print(b1)
print("상자의 부피는", b1.getHeight()*b1.getLength()*b1.getDepth())

#04
class Rectangle() :
    def __init__(self,x,y,w,h) :
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __str__(self) :
        return "("+str(self.x)+","+str(self.y)+","+str(self.w)+","+str(self.h)+")"

    def getArea() :
        return self.w * self.h

    def overlap(self,r) :
        if self.x < r.x and self.y < r.y :
            print("서로 겹칩니다.")
            return True
        else :
            print("겹치지 않습니다.")
            return False
                

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
r1.overlap(r2)

#05
class Triangle():
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

    numberOfSides=3
    
    def checkAngles(self):
        if self.angle1+self.angle2+self.angle3 ==180:
            return True
        else:
            return False

triangle=Triangle(90,30,60)
print(triangle.checkAngles())

#06
class Person() :
    def __init__(self,n=None,m=None,o=None,e=None):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

        
    def __str__(self) :
        return "("+str(self.name)+", mobile = "+str(self.mobile)+", office = "+str(self.office)+", email = "+str(self.email)+")"

    def setEmail(self, email) :
        self.email=email

p1 = Person("kim","1234567","kim@company.com")
print(p1)
p2 = Person("Park","2345678")
print(p2)
p2.setEmail("park@company.com")
print(p2)


#07
class Person():
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setMobile(self, number):
        self.mobile = number

    def setOffice(self, number):
        self.office = number

    def setEmail(self, address):
        self.email = address
        
    def __str__(self):
        s = ''
        s += self.name + '\n'
        s += "office phone:"+self.office + '\n'
        s += "email address:"+self.email + '\n'
        return s

class PhoneBook():
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None,email=None):
        p = Person(name, mobile, office, email)
        self.contacts[name] = p
    def __str__(self):
        s = ''
        for p in sorted(self.contacts):
            s += str(self.contacts[p]) + '\n'
        return s

obj = PhoneBook()
obj.add("Kim", office="1234567", email="kim@company.com")
obj.add("Park", office="2345678", email="park@company.com")
print(obj)

#08
class Song() :
    def __init__(self,song) :
        self.song = song
    def sing(self) :
        for i in self.song :
            print(i)

aSong = Song(["aaa","bbbb","ccc","dddd"])
aSong.sing()

#09
import turtle

lee = turtle.Pen()
park = turtle.Pen()


lee.shape("turtle")
lee.forward(100)
lee.right(90)
lee.forward(20)
lee.left(90)
lee.forward(100)


park.shape("circle")
park.forward(-100)
park.right(90)
park.forward(-20)
park.left(90)
park.forward(-100)

turtle.mainloop()
