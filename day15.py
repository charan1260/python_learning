def add(a, b):
    print('add function')
    c = a + b 
    return c #c=25
    pirnt('HI')
def sub(a, b):
    print('sub function')
    c = a - b
    return ##no return =None
def div(a, b):
    print('div function')
    c = a / b #no return =None
x = add(10, 15)   
y = sub(20, 10)   
z = div(25, 10)   
print(x)#add function 
print(y)#sub function 
print(z)#div function 
print()
#none

# #Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}')
    print(f'My age is {age}')
    print(f'My rollno is {rollno}')
detail('rakesh', 20, 'A101')
print()
detail(20, 'A101', 'rakesh')
print()
detail(age=20, rollno='A101', name='rakesh')
print()
detail(rollno='A101', age=20, name='rakesh')
def add(a, b=10, c=20):
    return a + b + c 
print(add(1))#31
print(add(1,2))#23
print(add(1,2,3))#6
print(add(c=3, a=1, b=2))#

#order of = in function def
# def sub(a=10, b, c):# error non default arguments follows default arguments
pass 
#order of = in function call.
# add(a=10, b, c)
#  error positional  arguments follows keyword  arguments
def f1(*a):
    print(a)#(1,2,3,4)
    print(type(a))#<class 'tuple'>
f1(1,2,3,4)

def f2(**a):
    print(a)#{'a':1,'b':2,'c': 3,'d':4}
    print(type(a))# class 'dict'>
# f2(1,2,3,4)# throws error
f2(a=1, b=2, c=3, d=4)