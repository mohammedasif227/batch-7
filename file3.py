#Eg:-3
# Take value of the length and breadth of a
# from user and check if it is square or not.
'''
length=int(input("enter the length"))
breadth =int(input("enter the breadth"))
if(length == breadth):
    print("it is square")
else:
    print("it is not a square")

#Eg:-4
# python program to check whether the
# given integer is a multiple of both 5 and 7
n=int(input("enter the number"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")

#!Eg:-5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to following criteria
  #cost price (in Rs)                 Tax
  #>100000                            15 % + discount 6%
  #>50000 and <= 100000               10%
  #<= 50000                           5%
price = int(input("enter the price: "))
total = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    amount=value*(15/100)
    total=value+amount
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is: ",total)

#---->elif
#Eg:-1
a = 7
b = 9
c = 3

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greter")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# Ask user to enter marks and print the corresponding grade.


marks=int(input("enter the marks: "))
if(marks>80):
    print("A")
elif(marks>60 and marks<80):
    print("B")
elif(marks>50 and marks<60):
    print("C")
elif(marks>45 and marks<50):
    print("D")
elif(marks>25 and marks<45):
    print("E")
elif(marks<25):
    print("F")
#!Eg:-6
# Accept the age of 4 people and display the oldest one

a=int(input("enter first person age"))
b=int(input("enter second person age"))
c=int(input("enter third person age"))
d=int(input("enter fourth person age"))
if(a>b and a>c and a>d):
    print(" a is oldest")
elif(b>a and b>c and b>d):
    print(" b is oldest")
elif(c>a and c>b and c>d):
    print(" c is oldest")
elif(d>a and d>b and d>c):
    print(" d is oldest")

# !---> short hand if else
#Eg:-1
a=9
b=6
#if a>b:
#   print("A")
#else:
#   print("B")
#?---> using sort hand if else
# * Rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

#print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent

char = input("enter the char: ")
#if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#    print("is a vowel")
#else:
#    print("its consonent")

#?OR

str1 = "aeiouAEIOU"
if char in str1:
     print("vowel")
else:
     print("consonent")

#! shorthand if else
char = input("enter the char: ")
str1 = "aeiouAEIOU"
print("vowel") if char in str1 else print("consonent")
'''
#!---> elif ladder using short hand if else
#Eg:-
# ? Find greatest among 3 varaibles using short hand if else
a = 8
b = 8
c = 9

#print("A is greatest") if a>b and a>c else print(""B is greatest")
# if b>a and b>c else print("C is greater")

# !------> looping

#looping can be implimented using
#for loop
#While loop


#--->For loop
#for loop is used for iteration, if we know the number of times the lop have to run
#It is used to iterate the iterables eg(string,list,tuple,etc...)


# todo--> syntax for loop
# ! for syntax in C
#for(1=0;1<10;i++){
#    printf("hello");
#}


# ! for syntax in python
#for userdefined_varaible in range(start, end, step): default step value is 1
#  statement
#  statement
#  statement


# ? Eg:-1
# to print the value from 1 to 10 using for loop

#for i in range(0, 10): #(n, n-1)
#    print(i)
# print("hello")

# ? Eg:-2
#for val in range(23, 50, 1):
#    print(val)

#for val in range(1, 15, 3):
#   print(val)


# !Eg:-3
# to decrement the value
#for val in range(10, 0, -1):
#    print(val)

#for val in range(10, 0, -2):
#    print(val)

#for val in range(10, 0, 1):
#    print(val) # no output

# ? Eg:4
#print the output of 7th multiplication table from 21 to 43
#for i in range (21, 43+1, 7):
#   print(i)

#for i in range(1, 10+1,1):
    #print("7", "x", i, "=",i*7)--->method:1
    #method:-2   
    #ans="7 x {} = {}"
    #print(ans.format(i, i*7))
    #method:-3
    #print(f"7 x {i} = {i*7}")
# ? Eg:-5
#break----> used to teerminate the loop
'''
for val in range(1, 10):
    if val == 6:
        break
    print(val)
    
Eg:-6
for val in range(1, 10):
    print(val)
    if val ==6:
        break
Eg:-7
for val in range(1, 10):
    if val ==6:
        print(val)
        break
'''

# ! continue
#Eg:1
'''
for val in range(1, 10):
    if val ==6:
        continue
    print(val)

for val in range(1, 30):
    if val == 6 or val == 8 or val ==21:
        continue
    print(val)
'''

# ! practise problems
# ? print the even number between 20 to 40

for i in range(20, 41):
    if(i%2==0):
        print(i)

#!----> While loop

# ?While is used when we do not know the number of times the loop have to run
# ? To iterate the non iterable elements while loop is used
# while loop syntax
# initialisation
#while condition:
#   statement
#   incre or decre

#! Eg:-1
# To iterate number from 1 to 10

#i = 0
#while i<11:
#    print(i)




      
















