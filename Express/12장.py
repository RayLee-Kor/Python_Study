#01
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self) :
        return "(%d, %d)" % (self.x, self.y)

class Point3D(Point):
    def __init__(self,x,y,z):
        super().__init__(x, y) # 부모클래스의 x,y을 받아옴
        self.z=z
    def __str__(self) :
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point=Point3D(1,2,3)
print(my_point)


#02

class Address :
    def __init__(self, street, city) :
        self.street = str(street)
        self.city = str(city)
        
class Person :
    def __init__(self,name,email) :
        self.name = str(name)
        self.email = str(email)

class Contact(Address,Person) :
    def __init(self, street, city, name, email) :
        super().__init__(street,city)
        super().__init__(name,email)
        


#03

import cmath # complex math 모듈
class Function:
    def __init__(self):
        pass
    def value(self, x):
        pass

class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def value(self, x):
        return (self.a)*x**2+(self.b)*x+(self.c)

    def get_roots(self):
        d = (self.b**2) - (4*self.a*self.c)

        sol1 = (-self.b-cmath.sqrt(d))/(2*self.a)
        sol2 = (-self.b+cmath.sqrt(d))/(2*self.a)

        print(f'solution: {sol1}, {sol2}')
e = Quadratic(1, 5, 6)
e.get_roots()


#04

import random
class Dice:
    def __init__(self,x) :
        x = self.x
        
    def roll() :
        x = random.randrange(1,7)
        print(x)
        return x

class FraudDice(Dice) :
    def __init__(self,x,y,z) :
        super().__init__(x)
        y = self.y
        z = self.z
        
    def roll() :
        y = random.randrange(1,7)
        z = random.randrange(1,7)
        Dice.roll()
        print(y)
        print(z)

Dice.roll()
FraudDice.roll()


#05

class Animal:
    def __init__(self, age):
        self.age=age

    def eat(self):
        print("동물이 먹고 있습니다. ")


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(age)
        self.name=name
        self.breed=breed


a = Cat("aaa", 2, "Pure")
b = Cat("bbb", 3, "Pure")
c = Cat("ccc", 5, "Pure")

def get_oldest_cat(*args):
    return max(args)

age = get_oldest_cat(a.age, b.age, c.age)
print(f"가장 나이가 많은 고양이는  {age} 살입니다.")


#06

class Course :
    def __init__(self, course,score) :
        self.course = course
        self.score = score
        
class Department(Course) :
    def __init__(self, dept) :
        self.dept = dept

    def add_course(dept,course, score) :
        super().__init__(course,score)
        return course


class Student(Department) :
    def __init__(self, name,number) :
        self.name = name
        self.number = number

    def enroll(score,course) :
       super().__init__(dept)
       print(course)

        
dept = Department("컴퓨터")
math1 = dept.add_course("공업 수학",3)
math2 = dept.add_course("이산 수학",2)

kim = Student("kim", 2020001)
kim.enroll(math1)


#07
class Song:
    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        artist.add_song(self)

class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist
        track_number = len(self.tracks)
        song = Song(title, artist, self, track_number)
        self.tracks.append(song)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

lee = Artist("Lee's Band")
album = Album("첫 번째 앨범", lee, 2020)
album.add_track("첫 번째 노래")
album.add_track("두 번째 노래")

playlist = Playlist("애창곡")

for song in album.tracks:
    playlist.add_song(song)
