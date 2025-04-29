#%%
print("hello")

#%%

print("나의 이름은?", "홍길동")
print("나의 나이는?" ,27)
print("나의 키는?", 175, "cm입니다")
print("10 + 20 = ", 10+ 20)
print("10 * 20 = ", 10 * 20)
#%%

print("hi" "hello")
print("hi","hello")

#%%
num1 = num2 = num3 = 200
print(num1, num2, num3)

num4, num5 = 300 ,400
print(num4, num5)

# %%
num = 85
print(type(num))
pi = 3.14159
print(type(pi))
message = "Good morning"
print(type(message))
# %%
print(7**2)
print(7%2)
print(7//2)
x = 7; x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 5
print(x)
x **= 2
print(x)
#%%
print(123 * 456)
print(1357 + 2458)
print(5 ** 4)
print(10 / 4)
print(10 // 5)

print(2 ** (1/2))
print(3 ** (1/3))
# %%
a, b = 100, 200
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
# %%
국어 = 80; 영어 = 75; 수학 = 55
print((국어 + 영어 + 수학) /3)
# %%
num = 13

if(num % 2 == 0) : 
    print("짝수")
else:
    print("홀수")
# %%
txt6 = "Let's go"
print(txt6)
# %%
long_str = """
사과는 맛있어
맛있는건 바나나
"""
long_str
# %%
b1 = "'"
b2 = '"'
b3 = "\'"
b4 = "\""
print("b1", b1, "b2", b2)
print("b3", b3, "b4", b4)
# %%
multiline = "Life is too short\n You need python"
print(multiline)
food = "Python\'s favorite food is perl"
print(food)
say = "\'Python is very easy\' he says."
print(say)
# %%
a1 ="\n"
print(a1)
# %%
listA = [1,2]
listB= [3,4]
print(listA + listB)
# %%
print("=" * 50)
print("My Program")
print("=" * 50)
# %%
a = "Life is too short, You need Python"
print(len(a))
print(a[0])
print(a[33])
print(a[-1])
print(a[0]+a[1]+a[2]+a[3])
print(a[0:4])
print(a[:4])
print(a[4:0])
print(a[19:34])
print(a[::2])
# %%
a=1
print(id(a))
a=2; b=2
print(id(a), id(b))
# %%
s1 = set([1,2,3])
s2 = set([1,2,3])
print(id(s1), id(s2))
# %%
print("%d" % 3)
# %%
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
print("rate is %f" % 3.234)
# %%
print("%0.4f" % 0.123456789)
print("%9.4f" % 0.123456789)
# %%
