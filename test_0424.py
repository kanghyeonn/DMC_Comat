
#%%
def is_odd():
    num = input("자연수를 입력해주세요.")
    if(int(num) % 2 == 0):
        print("짝수입니다.")
    else:
        print("홀수입니다.")

def avg(*nums):
    sum = 0
    for num in nums:
        sum += num
    print(sum / len(nums))
    

def gugudan(num):
    for i in range(1, 10):
        print(f"{num} * {i} =", num * i)

is_odd()
avg(1,2,3)
gugudan(2)
# %%
sum = lambda a , b: a + b
sum(3,4)
# %%
f = lambda: 1
f()
g = lambda x,y : x + y
g(1,2)
(lambda x: x**x)(3)
# %%
sub = lambda x, y: print(f"{x} - {y} = {x-y}")
sub(200,100)
# %%
def func(x):
    if x > 0:
        return x
    else:
        return x - 100
    
print(list(filter(func, range(-5,5))))
# %%
n_list = [-30, -45, -5, -90 ,20, 53, 77, -36]
minus_list = []
for n in filter(lambda n : n < 0, n_list):
    minus_list.append(n)
print("음수 리스트 :", minus_list)
# %%
minus_list = list(filter(lambda n : n < 0, n_list))
print('음수 리스트:', minus_list)
# %%
a = filter(lambda n : n < 0, n_list)
print(type(a))
# %%
print(a)
# %%
even_list = []
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in filter(lambda n : n % 2 == 0, n_list):
    even_list.append(n)
print(even_list)
# %%
even_list = list(filter(lambda n : n % 2 == 0, n_list))
print(even_list)
# %%
odd_list = []
for n in filter(lambda n : n % 2 != 0, n_list):
    odd_list.append(n)
print(odd_list)
# %%
odd_list = list(filter(lambda n : n % 2 != 0, n_list))
print(odd_list)
# %%
a_list = ['a', 'b', 'c']
def to_upper(n):
    return n.upper()

A_list = list(map(to_upper, a_list))
print(A_list)
# %%
A_list = list(map(lambda n : n.upper(), a_list))
print(A_list)
# %%
n_list = [10, 20, 30]
def twice(n):
    return n * 2
def triple(n):
    return n * 3
print(f'입력값의 두 배 : {list(map(twice, n_list))}')
print(f'입력값의 세 배 : {list(map(triple, n_list))}')
# %%
print(f'입력값의 두 배: {list(map(lambda n : n * 2, n_list))}')
print(f'입력값의 세 배: {list(map(lambda n : n * 3, n_list))}')
# %%
from functools import reduce
a = reduce(lambda x, y : x + y, range(1, 101))
print(a)
print(f'1에서 100까지의 합 : {reduce(lambda x, y : x + y, range(1, 101))}')
# %%
cubic = [n ** 3 for n in range(1, 11)]
print(cubic)
# %%
a = ['welcome', 'to', 'the', 'python', 'world']
first_a = [text[0] for text in a]
print(first_a)
# %%
text = input("문장을 입력해주세요 : ")
rmList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '-', '=', '?', '.', ',', '?', '<', '>', ';' , ':', '"', "'", '/']
strList  = list(filter(lambda word : word not in rmList, text))
strList = list(filter(lambda word : word != ' ', strList))
strList.sort()
print(strList)
# %%
print([int(x) for x in input('정수를 여러개 입력하세요 : ').split()])
# %%
cubic = [x**3 for x in range(1, 11) if x**3 <= 500]
print(cubic)
# %%
st = 'Hello 1234 Python'
print([c for c in st if c.isdigit()])
# %%
cr = input('3명의 국어점수(예 51,67,98)입력 : ')
k1, k2, k3 = eval(cr)
print(k1, k2, k3, '합계:', k1+k2+k3)
# %%
import os
os.getcwd() # get current working directory
# %%
import sys
print(sys.path)
# %%
f = open(os.getcwd() + '/fileTest.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()
# %%
filePath = os.getcwd() + '/fileTest.txt'
f = open(filePath, 'r')
line = f.readline()
print(line)
f.close()
# %%
f = open(filePath, 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
# %%
f = open(filePath, 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# %%
f = open(filePath, 'r')
data = f.read()
print(data)
f.close()
# %%
f = open(filePath, 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()
# %%
filePath2 = os.getcwd() + '/fileTest2.txt'
with open(filePath2, 'w') as f:
    words = ['Python\n', 'YUNDAHEE\n', '076923\n']
    f.write('START\n')
    f.writelines(words)
    f.write('EMD')
# %%
text = input("저장할 내용을 입력하세요:")
f = open(filePath2, 'a', encoding='UTF-8')
f.write(text)
f.write('\n')
f.close()
# %%
filePath3 = os.getcwd() + '/text.txt'
f = open(filePath3, 'w')
f.write('Life if too short\nyou need java')
f.close()
f = open(filePath3, 'r')
text = f.read()
text = text.replace('java', 'python')
f.close()
f = open(filePath3, 'w')
f.write(text)
f.close()
# %%
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
filePath4 = os.getcwd() + '/scores.txt'
f = open(filePath4, 'w')
for score in scores:
    f.write(str(score) + '\n')
f.close()
# %%
f = open(filePath4, 'r')
# data = f.read()
# score_list = data.split('\n')
# print(score_list)
sum = 0
i = 0
while True:
    line = f.readline()
    if not line:
        break
    sum += int(line.replace('\n',''))
    i += 1
avg = sum / i
print(avg)
f.close()
f = open(os.getcwd() + '/avg.txt', 'w')
f.write(str(avg))
f.close()
# %%
def my_sort(*number):
    li = list(number)
    li.sort()
    print(li)

my_sort(1,2,3,5,4)


# %%
