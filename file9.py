#Day-->9
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


# 2) program
'''
s1 = "Hello how are you"
s2 = "Hello how is"
s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
'''

# 3) program
'''
num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)
'''

# ! constructors
# ! Eg:2
#  * unparametarised constructor
'''
class profile:
    def __init__(self):
        print("Hello world")
obj = profile()
obj.__init__()
'''
# ? Eg:3
# * parametarised constructor
'''
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)
obj = profile(1, "Asif",26)
'''
# ? Eg:4
'''
class c1:
    email = "kasulamohammedasif@gmail.com"
    def m1(self):
        name = "Asif"
        place = "Ap"
        print(name, place)
        print(self.email)
object = c1()
object.m1()
'''
# ? Eg:4
'''
class c1:
    def m1(self):
        name = "asif"
        age = "26"
        return name,age
    def display(self):
        print(self.m1())
object = c1()
object.display()
'''
# ? Eg:5
'''
class class1:
    def __init__(self):
        name = "sid"
        email = "kasulamohammedasif@gmail.com"
    def display(self):
            print(self.name, self.email)
c1 = class1()
c1.display()
'''
# !-----> Inheritance
#The process of utilising the method and attributes of parent class
# Throught the object of child class it is called as inheritance

# 5 types of Inheritance
# single Inheritance
# multilevel Inheritance
# multiple Inheritance
# Hybrid Inheritance
# heirarichal Inheritance


# single Inheritance

# It has only one parent class and only one child class
# ! Eg:1
'''
class parent:
    def m1(self):
        print("Iam parent class")


class child:
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()
'''
#Eg:2
'''
class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()
'''
# Eg:3
'''
class parent:
    name = "Asif"

class child(parent):
    name = "name1"
    def display(self):
        print(self.name)
d = child
d.display()
'''

# ! Multilevel inheritance
# ? Eg:1
'''
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''

# ? Eg:2
'''
class honda_city:
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

    def amaze_body_specs(self, color, weight, height, length, vechical_type):
        print(color, weight, height, length, vehicle_type)

class Honda(civic):
pass

honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, "Hatchback")
'''

# ! Multiple Inheritance
# ? it has multiple paremt and 1 child
'''

class while_petrol:
    def function_w(self):
        print("used to Airplane")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
print("Petrols types")

p=petrol()
p.defanition()
p.function()
'''
# ! Eg:2
'''
class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substraction, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)
'''             
       
#! Heirarical inheritance.
#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
color="green"
taste= "sweet"
self.display(color,taste)

c=carrot()
c.carrot_specs()
c.weight("30gms")


# hybrid Inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
# ! Hybrid Inheritance
# ? The combination of above 4 inheritance is called Hybrid Inheritance
class c1:
    def m1(self):
        print("Class 1")

class c2(c1):
    def m2(self):
        print("Class 2")

class c3(c2):
    def m3(self):
        print("Class 3")

class c4(c2):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("i am m3 from c4")

class c5(c3):
    def m5(self):
        print("Class 4")  

class c6(c5, c4, c2, c1):
    def m6(self):
print("Class 4")
        
obj = c6()
obj.m3()
# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding

































    




































