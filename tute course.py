# c = int(input("celcuis : "))
# f = (c * 1.8) + 32
# print(f)
# lst = [1,2,3,3,4,6]
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# print(abs(-56557))
# print(pow(2,3))
# a = int(input(" enter the number : "))
# if (a > 4 ):
#     print(" a is greater than 4")
# elif (a >= 4 ):
#     print(" a is eqal to 4")
# else:
#     print("not greater than 4")
#
# lst =[1,2,3]
# sum_of_num = 0
#
# for i in lst:
#     sum_of_num = sum_of_num + i
# print(sum_of_num)
#
# city =["mumbai" , "pune ", "ujjain"]
#
# for i in range(len(city)):
#     print(city[2])
#
# marks = {'Ram': 90, 'Shayam': 55, 'Sujit': 77}
#
# for student in marks:
#     if student == 90 :
#         print(marks[student])
# else:
#     print ('No entry with that name found.')
#
#
# n= 3
# sum_of_num = 0
#
# i =1
# while i<=n:
#     sum_of_num = sum_of_num +i
#     i = i+1
# print(sum_of_num)
#
# i = 1
# while i <= 5:
#     print("heloo")
#     i = i + 1
#
# i = 5
# while i >= 1:
#     print("heloo")
#     i = i - 1
# for i in range(3,33,3):
#     print(i)
#
# for i in range(3,8):
#     print(i)
#     if i == 5:
#         continue
#     else:
#         print(i)
# def games():
#     print("ball")
#     print("bat")
#
# games()
# games()
# games()
#
# def add(a,b):
#     print(a+b)
# add(1,2)
#
# def sub(a,b):
#     c= a+b
#     return c
# re = sub(3,2)
# print(re)


#calling two function togher
# def sum(a,b):
#     return a+b
# def square(z):
#     return z*z
#
# vaps = square(sum(5,2))
# print(vaps)

# def fact(n):
#     if n < 2:
#         return 1
#     else:
#         return n * (fact(n-1))
#
# result = fact(2)
# print(result)
# print("hello")

# class car:
#     color = "black"
#     type = "suv"
# car1 = car()
# print(car1.color.isalpha())

# class emp():
#     increment = 1.5
#     def __init__(self,fname,lname,salary):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#
#     def increment():
#         pass
#
# harry = emp("raam","shaam",23)
# rohan = emp("harry" , "bhao",35)
#
# print(harry.salary,rohan.lname)

# class A:
#     def state_1(self):
#         print("char kelo metr")
#
#     def state_2(self):
#         print("char kela metr")
#
# class B(A):
#     def money(self):
#         print("char lakh")
#
# # a = A()
# # a.land()
# b = B
# b.state_2()

import re
pattern ="apple"
x = re.findall("apple",pattern)
print(x)

if re.match(pattern,"apple"):
    print("true")
else:
    print("false")