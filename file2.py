'''
- ---> Variables
a, b, c = 9, 8, 7, 8
print(a, b, c)

a, b=c=7, 8
print(a)
print(b)
print(c)

a=b, c=4,2
print(a, b, c)

#----->Swapping of variables
eg:1 a = 7
     b = 5
     temp=a
     a=b
     b=temp
     print(a,b)
eg:-2
     a=a+b #a=12
     b=a-b #b=12-7=5
     a=a-b #a=12-5=7
     print(a,b)
     
a, b=b, a #only in python
print(a,b)

a=7
b=5
a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))

#id()---->used to find the memory address of the variable
a=7
b=5
print(id(a))
print(id(b))
'''
#----->keywords
#keywords are reserved words which provides special meaning to
#compiler or interpretor

#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

#to check if the string is keyword or not
#print(keyword.iskeyword("sid")) #false

#if = 8
#print(if) #error coz if is a keyword

#!---->literals
#literal is the constant value assigned to a variable
#a variable is considers to constant when it is defines
#in caps
a=78 # a is variable
A=78 # A is constant

# hash()--->it creates a hash value for constant datatypes and
# provides error for non constant datatypes
#n1 = 89+7j
#print(hash(n1))

#f1 = [7, 8, 9]
#print(hash(f1)) # error--> list is non-constant or mutable datatype
#a=9
#b=9
#b=90
#print(id(a))
#print(id(b))

#!----> Operation
# Operation are symbol whic is used to perfrom various opearions
# between 2 or more operands


#Arithmatic
#logical
#relational or comparison
#Bitwise
#Identity
#Memberships

#!----> Arithmatic ---->+,-,*,/,%,//,**
#Eg:-1:-
#a = 8
#b = 6
#c = 9
#print(a+b+c)

#input()----> used to get the runtime input
# eval()----> used to get the runtime values of all datatype


#n1 = input("enter the value: ")
#print(n1)

# a = 4
# b = 2
#print(a/b) # is used to get the quotient value
#print(a%b) # is used to get the remainder value


#---->Floor division

#a = 765433
#b = 19
# print(a/b) #-> the output will be in integer & the output will be
# based on floor value


#! **---> used for powers of a number
# print(2**4) #-->16


#! Assignment --> +=, -=, /=, //=, **=, &=, |=
#a= 8
#a+=2
#print(a)

#a=30
#print(a)


#! Comparision--> ==,>,<,!=,<=,>=
#a=8
#b=7
#print(a>b) #true

#a = 9
#b = 5
#print(a==b)

#! Bitwise operator--> &, |,^,~,<<,>>
#a = 7
#b = 4
#print(a|b)

#OR
#A  B  A|B
#0  0   0
#0  1   1
#1  0   1
#1  1   1


#XOR
#A B A^B
#0 0  0
#0 1  1
#1 0  1
#1 1  0

#AND
#A B  A*B
#0 0   0
#0 1   0
#1 0   0
#1 1   1
# ~ -->

'''
a = 9
128 64 32 16 8 42 1
0   0  0  0  0 0 0 --->   9

1   1  1  1  0  1 1 0 # --> -10

0   0 0 0 1  0 1 0 1 0 #  --> 10
'''

# 1 1 1 1 0 1 0 1 --> 1s compliment of 10
              # 1 --> 2s compliment
#---------------------------------------
# 1  1  1  1  0 1  1 0  --> -10


# 256  128  64 32 16 8 4 2 1
# 107




# <<, >>
#print(5<<3)



# <<, >>
# print(5>>1)
#16>4


# ! Logical Operator
# and, or, not
#a = 6
# print (a>3 and a<10)
#print(a>7 or a< 30 )
#print(not(a>8 and a <10))


# ! Identity Operator
# is, is not
# are stored ?
'''
a = 8
b = 8
'''
#print(a is b)
#print(a == b)

'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)


# ! Membership Operator
# in not in
l1 =[7,8,9,0,6,5]
num = 55
print( num in l1)
print(num not in l1)

num = 678
print(8 in num) # error

# ! Conditional Statement
# if, elif, else


# Eg :1
#---> C syntax

if (condition){
    statement;
    statement;
    statement;
    statement;
}


Python Syntax

if condition:
    statement
    statement
    statement
    statement

Eg: 1
'''

'''
a=6
if a:
    print("Hello")
Eg:2    
'''
'''
a = 1
if a>3:
    print("yes")
else:
    print("no")
 '''
#if 5> 8:
  #  print("hello")
#else:
 #   print("no")


 # Eg:3
#if 7> 8:
  #  print("hello")
#else:
 #   print("no")



'''
Eg:4
a=0
a = None
a = False
a=""
if a :
    print("yes")
else:
    print("no")

 # a number is even or odd

n=int(input("enter the number"))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")
''''

#sum:2
#name, age, nationality
# 18 above,indian






name = input("enter the name: ")
age = int(input("enter the age: "))
nationality = input("enter the nationality")
if age>=18 and nationality == "Indian":
    print("eligible for vote")
else:
    print("not eligible")
























