# a=10
# b=5.5
# c="name"
# print(a)
# print(b)
# print(c)
# # check a variable
# x=10
# print(type(x))

# # same value to assign a multiple variables
# a=b=c=10
# print(a)

# # multiple values in single variable
# a=0,3,4,5
# print(a)

# # data tyes:
# # int :
# a=10
# b=4
# c=a+b
# print(c)

# # float
# a=3.3
# b=2.2
# print(a)
# print(b)
# print(a+b)

# # complex:
# a=3+2j
# b=3+3j
# c=a+b
# e=a*b
# print(e)
# print(c)
# d=a-b
# print(d)

# # n1=input("enter ur number")
# # n2=input("enter ur number")
# # print(n1+n2)


# # m=input("enter ur number")
# # print("welcome back"+m)


# # n1=int(input())
# # n2=int(input())
# # print(n1+n2)

# # 1) print ur name
# # 2) enter ur name with hello
# #3) add two numbers
# # Input one number and print its square.
# # 5)Input two numbers and print sum, difference, product, division.
# # 6) to create a student details

# # print("name")
# # n=input()
# # print("hello"+n)
# # n=int(input())
# # print(n*2)
# # n1=int(input())
# # n2=int(input())
# # print(n1+n2)
# # print(n1-n2)
# # print(n1*n2)
# # print(n1%n2)


# s={"name":"raju","place":"guntur","dept":"ece"}
# s["name":"rajuuu"]={"name":"rajuu"}
# print(s)

# n=int(input())
# i=1
# while i<=n:
#     print(i)
# i=i+1


# print 1 to 100 numbers in while
# n=int(input())
# i=1
# while i<=n:
#     print(i)
#     i=i+1


# n=int(input())
# c=0
# while n!=0:
#     n=n//10
#     c=c+1
#     print(c)

# n=int(input())
# c=0
# while n>0:
#     n=n//10
#     c=c+1
#     print(c)


# n=int(input())
# c=0
# while n>0:
#     n=n//10
#     c=c+1
#     print(c)

# sum of individual digits are there
# n=int(input()) 
# s=0 
# while n!=0:
#     d=n%10 
#     s=s+d 
#     n=n//10 
#     print(s)
# print 1 to n numbers
# n=int(input())
# i=1
# while i<=n:
#     print(i)
#     i=i+1
# in given numbers is count in while
# n=int(input())
# c=0
# while n!=0:
#     n=n//10
#     c=c+1
#     print(c)
# sum of individual digits are of a given number

# n=int(input()) user can give the data
# s=0   sum is zero im taken
# while n!=0: given the number is not equal to the zero
#     d=n%10 digit it gives the last number
#     s+=d  count the sum for every iterartion 
#     n=n//10 n=n//10 it givees the last number
#     print(s) and print the sum


# CHECK GIVEN NUMBER IS PALINDROM OR NOT

# n=int(input())
# t=n
# r=0
# while n!=0:
#     d=n%10
#     r=r*10+d
#     n=n//10
# if t==r:
#     print("palindrome")
# else:
#     print("not a palindrome")

# n=int(input())
# t=n
# r=0
# while n!=0:
#     d=n%10
#     r=r*10+d
#     n=n//10
# if t==r:
#     print("palindrome")
# else:
#     print("not a palindrome")


# n=n//10  it removes a last number
# d=n%10 it gives a last digit
# s=s+d it will sum add and count

# display maximum number from a given number

# n=int(input())
# max=0
# while n!=0:
#     d=n%10
# if d>max:
#     max=d
#     print(max)

# l=[1,2,3,4,5,6]
# print(5 in l)
# print(8 in l)    


# HOW TO CREATE A LIST
# l=[1,2,3,4,5]
# print(l)


# how to access a list from verticalline

# l=[1,2,3,45,45,6]
# for i in range(len(l)):
#     print(l[i])


# given list how many characters are there
# l=[1,2,3,4,5,6,6]
# print(len(l))

# how to adda  a element in list at end position
# l=[1,2,3,4,5,6]
# l.append(67)
# print(l)

# how to delete a number from a list
# l=[1,2,3,4,56,34]
# l.pop(2)
# print(l)

# how to add particular specific position
# l=[1,2,3,4,5,6]
# l.insert(2,45)
# print(l)


# how to remove a particular elememt from a list
# l=[1,2,3,4,5,6]
# l.remove(4)
# print(l)

# how to reverse a list
# l=[1,2,3,4,5,6]
# l.reverse()
# print(l)

# how to sort a list from ascending order
# l=[1,22,32,55,5,6]
# l.sort()
# print(l)

# how to sort a list from discending order
# l=[1,22,3,890,6464,5,736,66,66]
# l.sort(reverse=True)
# print(l)

# creating a list with different datatypes
# l=[1,2,3,4,5,"name",3.4] 
# print(l)

# list compression
# syn:[exp for  var in seq]
# n=int(input())
# l=[int(input()) for i in range(n)]
# print(l)

# how to access a list from index
# l=[1,2,3,4,5,5,6]
# print(l[0])
# l[3]=45
# print(l)

# how to search  a number in list
# l=[1,2,3,4,5,5,66,7]
# print(5 in l)
# print(100 in l)

# l=[1,2,3,4,5,6]
# print(len(l))
# l=int(input())
# for i in range(5):
#     print([i])

# creating a list when inputs line by line
# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
#     print(l)

# l=list(map(int,input() .split()))
# print(l)

# n=map(int(input()))
# l=list(map(int,input().split()))
# print(l[n-1])

# for i in range(len(n)):
#     print(n[i])

# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
#     print(l)

# l=list(int,input().split())
# print(l)

# l=[1,2,3,4,5]
# for el in  l:
#     print(el)

# creating a list when inputs are line by line
# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
#     print(l)

# to print a list

# l=[1,2,3,4,5]
# for i in range(len(l)):
#     print(l[i])

# l=[]
# for el in input().split():
#     l.append(int(el))
#     print(l)

# l=[int(el) for el in input().split()]
# print(l)
# how many times repeated in a given list
# l=[1,2,3,4,4,5]
# print(l.count(5))


# l=list((int,input()).split())
# s=0
# for el in l:
#     s=s+el
#     print(s)




l=[1,2,3,4,5]
# l.remove(3)
# # l.pop(2)
# del[l[2]]
print(l)











