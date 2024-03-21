#Day-->10
# ploymorphism in classes
# We can achieve polymorphism in 2 ways
# 1)Method overloading-->It is not possible in python
# 2)Method overriding

# ! Method riding
# * ploymorphism in classes
#Eg:1
'''
class bank:
    def ratio(self):
        print("All bank has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()
'''
# !Eg:2
'''
class USA:
    def language(Self):
        print("English")


    def capital(Self):
        print("Washington Dc")

class India(USA):
    def language(Self):
        print("None")

    def capital(Self):
        print("New delhi")

I = India()
I.language()
I.capital()
'''
#Eg:3
# polymorphism using object

#c1, c2-->c1=print(c1),print(c2)
# f1,f2
'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj1.f1()

obj2 = c1()
obj2.f1()
'''
#Eg:4
'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)
'''
# * changing the functionality of builtin function
#Eg:5
'''
class shopping:
    def __init__(self,l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shopping([1,2,3,4,5])
print(len(s))
'''
# !---->Method overloading
# !Eg:1
'''
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
#s.add(4, 3) #!--->error
s.add(4, 5, 1)
'''

#Eg:2
'''
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and  b!=None:
            print(a+b)
        else:
            print(a)
obj = summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)
'''

# !-----> Abstraction
#The process of hiding the implimentation details is abstraction

#Eg:1
#class shapes:
#    def sides(self):
#        print('All shapes have sides except circle')

#class triangle:
#    def triangle_sides(self):
#        print("3 sides")
#class square:
#    def square(self):
#        print("4 sides")
#    def sides(self):
#        pass

#s = shapes()
#s.sides()

#tr = triangle()
#tr.triangle_sides()

'''
def decor(func):
    def inner():
        str1 = func()

def greet():
    return 'good morning'

print(decor(greet))
'''

# ! Rules to define abstract class 1
#1.) Abstract class cannot be instantiated
#2.) From abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) Convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes
#Eg:2
# super() ---. used to access the parent class method from child class method
'''
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
class2 = c2()
class2.m2()
'''
#Eg:3
'''
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd
    

class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)
'''
# ! encapsulation
#Eg:1
'''
class car:
    __name = "BMW" #private variable
    print(__name)
    
c1 = car()
print(c1.name) #error
c1.name = "Audi"
print(c1.name) #error
'''
#-->Eg:2
# accessing private date outside the class
'''
class c1:
    __phone = '9876543210'

    def display(self):
        print(self.__phone)

c = c1()
c.display()
'''
#-->Eg:3
# ? declare private method
'''
class class1:
    def __m1(self):
        print("Iam private method")
    def __init__(self):
        self.__m1()
c = class1()
'''
# ? nested class
'''
class class1:
    class class2:
        name = "Asif"

        def display(self):
            print(self.name)
    obj1 = class2()
obj = class1()
obj.obj1.display()
'''




























































