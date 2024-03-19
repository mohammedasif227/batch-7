#day-->7
'''
def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("ASif", 21,"KSRM")
'''
# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement


#def f1():
# z = 8
#f1()
#print(z) #error--> cannot use outside ther function
'''
def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
# 1 problem
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("enter the value: "))
palindrome(a)
'''

# ? Based on the declaration of parameter and args
# ? Function are divided into categories
#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args



# Positional args

# Eg:-1
#? The position of parameter have to be same as position as argument
'''
def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
profile(9177951268,"asif", 98) # unexpected output
'''
# * Keyword args
# ! Eg:-1
# To overcome the disadvantage of position args,we use keywords args
# It is the process of initialising the parameters with the args while calling the
# function
'''
def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
profile(name ="asif",mark=96,phone=1234567890)
'''
# Exception of keyword args function
'''
def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
#profile(name ="asif", 12345678,  mark=96)# error--> positonal args follow keywords args
#profile(12345678,name ="asif",mark=96)# error--> name has multiple values
profile(name ="asif",mark=96,phone=12345678)
'''

# * Default args
# ! Eg:-1
# The method of assigning the argument to the parameter while declaring the function
'''
def profile(name,phone,place="kadapa"):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,place))
profile("asif",123456789)
'''
# ! Eg:-2
'''
def profile(name,phone,place="kadapa"):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,place))
profile("asif",123456789,"guntur")
'''
#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.

#(*>#): positive integer
#(#>*): negative integer
#(#=*): 0
#Example 1:
#Input 1:

###***   -> Value of S
#Output :

#0   → number of * and # are equal

#!Eg:-2
'''
def profile(name,phone,place="kadapa"):
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
        txt= "my name is {}. my phone number is{}.i got {}marks."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("asif",123456789,)
'''

# ! Eg:-2
'''
def profile(*name,age):
    for val in name:
        print("my name is",val, "may age is",age)
profile("sid", 'name2', 'name3', 28)# error--> age has no args
'''

# * Keyword varaible length args
# kwargs-->which is used to provide the args in the form of key value pair.
# ! Eg:-1
'''
def price(**price_list):
    print(price_list)
price(shirt=1000, iphone=80000)
'''

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5.25}
'''
n = int(input("enter the number: "))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
    print(d1)

def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)
'''

# !--->Object oriented programming
# The panadigms of object oriented progarming are

# class
# object
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object

#l1 = [1, 2, 3, 4, 5, 6]


# ? Eg:-1
'''
class c1:
    name1 = "Asif"
    print(name1)

# ?Eg:2
class person:
    name = "Asif"


c = person() # c as object
the proccess of creation of an object is called as Instantiation
print(c.name)
'''

# ? Eg:-3
#Create of a method
# When the function is created with a class is called as method
'''
class person:
    def display(person): # It is a method
        print("Hello Welcome to classes")
p = person()
p.display()
'''

#? Eg:4
# ! Method with parameter
'''
class person:
    def display(person, name, age):
        print(name, age)
p = person()
p.display("Asif",26)
'''

# ! Eg:-5
'''
class person1:
    fname = "Asif" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.fname)

    def full_name(person):
        print(person.fname+" " +person.lname)

p = person1()
p.first_name()
p.full_name()
'''
#! Eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation
'''
class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught this process
p.__init__()
'''
















