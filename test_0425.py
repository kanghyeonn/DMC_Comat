#%%
import numpy
# %%
import mod1_0425

print(mod1_0425.sum(3,4))
# %%
print(mod1_0425.safe_sum(3,4))
print(mod1_0425.safe_sum(3, 'a'))
# %%
from test_package import say_hello, say_goodbye
say_hello.hello()
say_goodbye.goodbye()
# %%
import sys
import os

sys.path.append(os.getcwd())
print(sys.path)
# %%
sys.path.remove(os.getcwd())
print(sys.path)
# %% 
import pandas as pd

csv_data = pd.read_csv("Catalog_v2.csv", header=None)
print(csv_data[0][0])
# %%
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("멍멍~~")
    
    def __str__(self):
        return f"my_dog의 이름은 {self.name}이고, 나이는 {self.age}입니다."

my_dog = Dog('Mango', 3)
my_dog.bark()
print(my_dog)
# %%
class Counter:

    def __init__(self, number = 0):
        self.number = number

    def reset(self):
        self.number = 0
    
    def inc(self):
        self.number += 1
        if(self.number >= 100):
            self.number = 0

    def dec(self):
        self.number -= 1
        if(self.number <= -1):
            self.number = 0
    
    def __str__(self):
        return f"C({self.number})"

c1 = Counter(10)
c1.inc()
print('c1 =', c1)
c2 = Counter()
c2.inc()
c2.inc()
c2.dec()
print('c2 =', c2)
c1.reset()
print('c1 =', c1)
# %%
class BankAccount:

    def __init__(self, name, account_num, balance = 0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print(f"{money}원이 입금되었습니다. 잔고는 {self.balance}원입니다.")

    def withdraw(self, money):
        if self.balance < money:
            print(f"계좌 잔고는 {self.balance}원으로 인출 요구 금액 {money}원보다 적습니다.")
        else:
            self.balance -= money
    
    def __str__(self):
        return f"{self.name}님의 계좌 {self.account_num}의 잔고는 {self.balance}원입니다."

account1 = BankAccount("홍길동", "1234-0001")
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)
# %%
class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def set_korean_quiz(self, korean_quiz):
        self.korean_quiz = korean_quiz
    
    def get_korean_quiz(self):
        return self.korean_quiz
    
    def set_math_quiz(self, math_quiz):
        self.math_quiz = math_quiz
    
    def get_math_quiz(self):
        return self.math_quiz

    def set_science_quiz(self, science_quiz):
        self.science_quiz = science_quiz
    
    def get_science_quiz(self):
        return self.science_quiz

    def set_total_score(self):
        self.sum = self.get_korean_quiz() + self.get_math_quiz() + self.get_science_quiz()
        return self.sum

    def get_avg_score(self):
        return self.sum / 3

    def __str__(self):
        return(f"이름 : {self.get_name()}, 학번 : {self.get_student_id()}\n국어성적 : {self.get_korean_quiz()}, 수학성적 : {self.get_math_quiz()}, 과학성적 : {self.get_science_quiz()}\n합계 : {self.set_total_score()}, 평균 : {self.get_avg_score()}")

name = input("학생의 이름을 입력하세요 :")
student_id = input("학생의 학번을 입력하세요 : ")
student = Student(name, student_id)
korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)
# %%
class Calculate:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculate(Calculate):
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculate):
    def add(self, val):
        super().add(val)
        if self.value >= 100:
            self.value = 100

cal = UpgradeCalculate()
cal.add(10)
cal.minus(7)
print(cal.value)

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)
# %%
class Calculator:

    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        self.total = 0
        for num in self.nums:
            self.total += num
        return self.total
    
    def avg(self):
        return self.total / len(self.nums)
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
# %%
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("background.jpg")

out = img.filter(ImageFilter.BLUR)
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250,250, image=tk_img)
window.mainloop()
# %%
import tkinter as tk
def open():
    pass

def quit():
    window.quit()

window = tk.Tk()
menubar = tk.Menu(window)
filtermenu = tk.Menu(menubar)

filtermenu.add_command(label="열기", command=open)
filtermenu.add_command(label="종료", command=quit)

menubar.add_cascade(label="파일", menu=filtermenu)

window.config(menu=menubar)
window.mainloop()
# %%
from random import randint
import os

f = open(os.getcwd() + "/random_numbers.txt", 'w')

for i in range (0, 10):
    f.write(str(randint(1,1000)) + " ")

f.close()

# %%
# %%
