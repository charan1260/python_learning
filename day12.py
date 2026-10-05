#*
#* *
#* * *


for row in range(1,4):
    for col in range(1,4):
        if col<=row:
         print("*",end=" ")
    print()
2nd pattern 
n = int(input())
 

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()
3rd pattter
n =5
for row in range(1,n+1):
    for col in range(1,n+1):
        if col==1 or col== n or row ==1 or row ==n: 
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
print()
 #4 th pattern 
n=5
for row in range(1,n+1):
   for col in range(1,n+1):
         if row +col==n:
             print("x",end=" ")      
         else:
             print(" ",end=" ")