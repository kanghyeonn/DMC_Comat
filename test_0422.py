#%%
txt1 = "I ate {0} apples".format(3)
print(txt1)
number = 3; day = 2
txt2 = "I ate {0} apples. so I was sick for {1}".format(number, day)
print(txt2)
# %%
txt3 = f"I ate {number} apples. so I was sick for {day}"
print(txt3)
# %%
a = ','
print(a.join('abcd'))
# %%
a = "Life is too short"
print(a.split())
a= "a:b:c:d"
print(a.split(":"))
# %%
str1 = "881120-1088324"
print(str1[0:6], str1[7:])
# %%
print(str1[7])
# %%
a = "a:b:c:d"
print(a.replace(':', ';'))
# %%
url = "https://dmcportal.kr/"
url1 = url[8:]
url2 = url1[:url1.find(".")]
pw = url2[:3] + str(len(url2)) + str(url2.count('e')) + '!'
print(pw)
# %%
aa = list(range(10))
print(aa)
# %%
a = list(range(15))
print(a)
# %%
a_list1 = a[0:5]
print(a_list1)
# %%
a_list2 = a[5:11]
print(a_list2)
# %%
a_list3 = a[11:]
print(a_list3)
# %%
a_list4 = a[2:11:2]
print(a_list4)
# %%
a_list5 = a[10:5:-1]
print(a_list5)
# %%
a_list6 = a[10:0:-2]
print(a_list6)
# %%
a = list(range(1,11))
print(f"nList = {a}")
a.insert(0,0)
print(f"nList = {a}")
b = a[len(a)::-1]
print(f"nList = {b}")
a.reverse()
print(f"nList = {a}")
print(f"마지막 원소 = {a.pop(len(a) - 1)}")
print(f"nList = {a}")
# %%
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(a[4], a[2])
# %%
a = ['Life', 'is', 'too', 'short']
print(" ".join(a))
# %%
a = [1,2,3]
print(len(a))
# %%
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
# %%
a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(4)
print(a)
b = a
print(b)
print(id(a), id(b))
# %%
a = (2,3)
b = a
print(b)
print(id(a), id(b))
# %%
t_fruits = ('apple', 'orange', 'water melon')
print("변경 전:", t_fruits)
f_list = list(t_fruits)
f_list[1] = "kiwi"
f_fruits = tuple(f_list)
print("변경 후:", f_fruits)
# %%
person = {'이름':'홍길동', '나이': 26, '몸무게': 82}
print(person['이름'])
print(person['나이'])
print(person['몸무게'])
person['직업'] = '율도국의 왕'
print(person['직업'])
person['나이'] = 27
print(person['나이'])
del person['직업']
dic = {'이름' : '1', '이름' : '2', '이름': '345'}
print(dic)
print(dic.get('나이'))
print(dic['이름'])
# %%
dic1 = {'name' : '홍길동', 'birth' : 1138, 'age' : 30}
print(dic1)
# %%
a = {'A' : 90, 'B' : '80', 'C' : 70}
print(a.pop('B'))
print(a)
# %%
print(a.get('B', '80'))
print(a)
# %%
a = {'A' : 90, 'B' : 80, 'C' : 70}
listA = list(a.values())
listA.sort()
print(listA[0])
# %%
a=b=c=2
print(a)
# %%
num_a = 100; num_b = 200
if num_a == num_b:
    print("두 값이 일치합니다")

num_c = 300; num_d = 300
if num_c == num_d:
    print("두 값이 일치합니다")
# %%
game_score = 800
if game_score >= 1000:
    print("당신은 고수입니다")

game_score1 = 1300
if game_score1 >= 1000:
    print("당신은 고수입니다")
# %%
num = input("정수를 입력하세요 : ")
print(f"n = {num}")
n = int(num)
if n % 2 == 0:
    print(f"{n} 은(는) 짝수입니다.")
else:
    print(f"{n} 은(는) 홀수입니다.")
# %%
num2 = input("정수를 입력하세요 : ")
print(f"x = {num2}")
if int(num2) > 0 :
    print(f"{num2} 은(는) 자연수입니다.")
else:
    print(f"x = {num2}")
# %%
num3 = input("숫자를 입력하세요: ")
num3 = int(num3)
if num3 >= 1 and num3 < 11 :
    print(True)
# %%
num4 = input("나이를 입력해주세요:")
num4 = int(num4)
if num4 > 10 and num4 < 19:
    print("청소년입니다")

# %%
num5  = input("점수를 입력해주세요:")
num5 = int(num5)
if num5 >= 90 and num5 <= 100:
    print("A")
elif num5 >= 80 and num5 < 90:
    print("B")
elif num5 >= 70 and num5 < 80:
    print("C")
elif num5 >= 60 and num5 < 70:
    print("D")
else:
    print("F")
# %%
