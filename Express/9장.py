#9장
#불필요한 내용이 많아 필요한 부분만 정리하였습니다.

#01

from tkinter import *
window = Tk()
window.title("Welcome to tkinter")
window.geometry('200x40')
lbl = Label(window, text="Hi!")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="clicked")
btn = Button(window, text="click me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

#02

from tkinter import *
window = Tk()
window.title("Welcome to tkinter")
window.geometry('400x50')
lbl = Label(window, text="Hello, I'm Label!",height=3,width=50,background="orange",foreground="blue")
lbl.pack()
window.mainloop()


#03

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(10):
        button = tk.Button(window, text=f"{i}행,{j}열")
        button.grid(row=i, column=j)

window.mainloop()


#05

import tkinter as tk
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()
#window.geometry('300x40')

btn_decrease = tk.Button(master=window, width=10, text="감소", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, width=10, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, width=10, text="증가", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()


#06

import tkinter as tk
import random

value =0

def numbers() :
    v.delete('all')
    value = int(random.randint(0,6))
    v.create_text(150,50,text=value)

window = tk.Tk()

v = tk.Canvas(master=window, width = 250, height = 100)
v.grid(row=0, column=0)
v.create_text(150,50,text=value)

randbutton = tk.Button(master=window, width=10, text="굴리기", command=numbers)
randbutton.grid(row=0, column=1)


window.mainloop()


#07

from tkinter import *

def do_convert():
    inch_val = float(cvt_from.get())
    centimeters_val = inch_val * 2.54
    cvt_to.set('%s 센티미터' % centimeters_val)

root = Tk()
cvt_from = StringVar()
cvt_to = StringVar()

from_lbl = Label(root, text='인치를 입력하시오:')
from_lbl.grid(row=0, column=0)
from_entry = Entry(root, textvariable=cvt_from)
from_entry.grid(row=0, column=1)

to_lbl = Label(root, text='변환결과:')
to_lbl.grid(row=1, column=0)
result_lbl = Label(root,
textvariable=cvt_to)
result_lbl.grid(row=1, column=1)

convert_btn = Button(root,
text='변환!', command=do_convert)
convert_btn.grid(row=3, column=1)
root.mainloop()


#09

from tkinter import *
fields = '이름', '직업', '국적'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e)))  
b1 = Button(root, text='Show',
        command=(lambda e=ents: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)
root.mainloop()


#11

import time
from tkinter import *

window = Tk()

canvas = Canvas(window, bg = "white", width = 300, height = 200)
canvas.pack()

id = canvas.create_text(10, 100, text = "파이썬 커피샵으로 오세요!")

while True:
    canvas.move(id, 2, 0)
    window.update()
    time.sleep(0.05)


#13
from tkinter import *

def left(event):
    canvas.move(id, -5, 0)

def right(event):
    canvas.move(id, 5, 0)

def down(event):
    canvas.move(id, 0, 5)

def up(event):
    canvas.move(id, 0, -5)

window = Tk()

frame = Frame(window, width=500, height=300)
frame.bind('<Left>', left)
frame.bind('<Right>', right)
frame.bind('<Up>', up)
frame.bind('<Down>', down)
frame.focus_set()
frame.pack()

canvas = Canvas(frame, bg = "white", width = 500, height = 300)
canvas.grid(row=0, column=0, columnspan=4)
id = canvas.create_rectangle(100, 100, 200, 200, fill = "blue")

window.mainloop()