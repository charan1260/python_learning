#Datatypes
#Integer
n = 123
print(n)         #123
print(type(n))   #<class 'int'>
a=123     #error   
a = 0b1011
b = 0o761
c = 0xF109
print(a)         #value=123
print(type(a))   #<class 'int'>
print(b)         #value=497
print(type(b))   #<class 'int'>
print(c)         #value=61705
print(type(c))   #<class 'int'>

# #Float
a = 12.34
b = 12.34e2
c = 12.34e-2
print(a, type(a))  #12.35 <class 'float'> 
print(b, type(b))  #1234.0 <class 'float'>
print(c, type(c))  #0.1234 <class 'float'>

# #Complex
a = 3 + 4j
b = 0j
c = 7j 
print(a, type(a), type(a.real), type(a.imag))# (3+4j) <
print(b, type(b), type(a.imag)) 
print(c)

# #Bool
a = True
b = False
print(type(a))#class ''bool'
print(type(b))#class ''bool'
c = a + b
print(c)#1
print(type(c))#class  'int'

# #NoneType
a = None
print(a)
print(type(a))#class 'None type

#List
a = []
b = list() 
c = [1,2,3,4,5]
# d = list(1,2,3,4,5)#error
e = list((1,2,3,4,5))
f = list('rakesh')
g = list(range(1,6))
h = list({1,2,3,4,4,5})
i = list({1:'a', 2:'b', 3:'c'})
print(a, type(a))#[] <classs 'list'>
print(b)#[]
print(c)#[1,2,3,4,5]
# print(d)
print(e)#[1, 2, 3, 4, 5]
print(f)#['r', 'a', 'k', 'e', 's', 'h']
print(g)#[1, 2, 3, 4, 5]
print(h)#[1, 2, 3, 4]
print(i)#[1, 2, 3]

# #Tuple
a = (1,2,3,4,5)
b = 1,2,3,4
c = True, 1, 3j, None
#     
d = (5.6)
e = (1+3j)
f = (1)
g = (True)
h = (3j)
i = 1,
j = True,
k = 3j,
l = tuple() 
# m = tuple(1,2,3,4,5) #error
n = tuple([2,3,4])
o = tuple({4,5,6})
p = tuple({1:'a', 2:'b', 3:'c'})
q = tuple(range(1,6))
r = tuple('rakesh')
print(a, type(a))#(1,2,3,4,5)<class 'tuple'>
print(b, type(b))#(1, 2, 3, 4) <class 'tuple'>
print(c, type(c))#(True,)
print(d, type(d))#5.6 <class ''float'>
print(e, type(e))#(1+3j) <class 'complex'>
print(f, type(f))#1 <class 'int'>
print(g, type(g))#True <class 'bool'>
print(h, type(h))#(3j) <class 'compllex'>
print(i, type(i))#(1,) <class 'tuple'>)
print(j, type(j))#True <class 'tuple'>
print(k, type(k))#(3j,) <class 'tuple'>   
print(type(l))#class 'tuple'>
# print(m) 
print(n)#(2,3,4)
print(o)#(4,5,6)
print(p)#(1,2,3)
print(q)#(1,2,3,4,5)
print(r)#('r', 'a', 'k', 'e', 's', 'h')

# #Set 
a = {}
b = set() 
c = {1,2,3,4}
d = {1,1,2,2,2,3,3,3,4,4,4,4}
# e = {[1,2,3], 4, True} #A tuple can be stored in a set; a list cannot.
# f = {{1,2,3}, 4, True}#Inner sets are mutable, so they cannot be elements of a set.
# g = {{1:'a', 2:'b'}, 4, True}#A dictionary is mutable too, so it cannot be an element of a set:
h = {(1,2,3),3.13, True, 4} 
i = {'rakesh', 4, True}
# j = set(1,2,2,3,3,4,4,4)#set() accepts only one iterable argument, not many separate values.
k = set([1,2,2,3,3,3])
l = set((4,4,5,5,6,6))
m = set({1:'a', 1:'b', 1:'c'})
n = set('rraakkeesshh')
o = set(range(1,6))
print(a, type(a)) #{} <class 'dict'>
print(b, type(b))#set() <class 'dict'>
print(c) #{1,2,3,4}
print(d, type(d))#{1,2,3,4} <class 'set'>
# print(e)#error
# print(f)#error
# print(g)#error
print(h)#{(1, 2, 3), 3.13, True, 4}
print(i)#{'rakesh',4,True}
# print(j) #error
print(k)#{1,2,3}
print(l)#{4,5,6}
print(m)#{1}
print(n) #{r,a,k,e,s,h}
print(o) #{1,2,3,4,5}

#Dict 
a = {}
b = dict() 
c = {1,2,3,4,5}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
# e = {[1,2,3]:'a', 2:'b'}
# f = {{1,2,3}:'a', 2:'b'}
g = {'rakesh':'a', 2:'b'}
h = {(1,2,3):'a', 2:'b'}
i = {1:'a', 1:'b', 1:'c', 2:'x', 2:'y'}
# j = dict(1,2,3,4,5)
# k = dict(1:'a', 2:'b')
l = dict({1:'a', 2:'b'})
m = dict([(1,2), [3,4], (5,6)])
n = dict( ((1,2),[3,4])) 
print(a, type(a))#{} <class 'dict'>
print(b)#{}   <class 'dict'>
print(c) #{1,2,3,4,5}
print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)
# print(j)
# print(k)
# print(l)
# print(m)
# print(n)

# #String
# a = 'rakesh'
# b = "rakesh"
# c = '''r
# a
# k
# esh'''
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c)) 

# #Range/

# #Slicing
# a = [4,1,2,3,5] 
# print(a[:])
# print(a[:3])
# print(a[2:])
# print(a[::-1])
# print(a[:3:-1])
# print(a[3::-1])
# b = {3,2,4,6}
# print(b[:3])
# c = {1:'a', 2:'b', 3:'c'}
# print(c[:2])
