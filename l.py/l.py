# l=[1,2,3,4,5,5,6]
# l[0]=2
# print(l)

# t=(1,2,3,4,5,5,6)
# t[1]=10
# print(t)
# n=int(input())
# if n<2:
#     print("not a prime")
# else:
#     for i in range(2,n):
#         if n%2==0:
#             print("not a prime")
#             break
#         else:
#             print("prime")
# n=int(input())
# if n<2:
#     print("not a prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#             break
#         else:
#             print("prime number")


# n=int(input())
# for i in range(1,n+1):
#     print(i)

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print(s)


# n=int(input())
# f=1
# for i in range(1,n+1):
#     f=f*i
#     print(f)

# n=int(input())
# for i in range(1,n+1):
#     if n%2==0:
#         print(i)


# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)


# n=int(input())
# for i in range(1,n+1):
#     print(i)

# user can given input
# i value to iterate the range 1 to n chang the values
# print the i values

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print(s)

# from errno import EUSERS


# CALCULATE SUM OF TWO EUSERS

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print(s)

# class demo:
#     def disp(self):
#         print("demo class",self)
# obj1=demo()
# obj2=demo()
# print(obj1)
# print(obj2)
# obj1.disp()
# obj2.disp()

# l=[1,2,3,4,56]
# l.append(20)
# l.extend([23,45,66,77,88])
# l.remove(56)
# l.pop(2)
# print(l[3])



# class A:
#     def show(self):
#         print("This is class A")

# class B(A):
#     def show(self):
#         print("This is class B")

# obj = B()
# obj.show()
# # obj.show()

# inheritance:
# class A:
#     def disp(s):
#         print("hlo hi this is raju")
# class B(A):
#     def disp(s):
#         super().disp()
#         print("raju here")

# obj=B()
# # obj=A()
# obj.disp()

# single line inheritance

# int: 
a=10
b=10
c=a+b
print(c)

a=10
b=5
c=a-b
print(c)

a=10
b=5
print(a/b)   
# it gives a float point

a=10
b=6
print(a//b)

a=10
b=6
print(a%b)



a=10
b=11
print(a>b)
print(a<b)
print(a>=b)



a=10
b=10
print(a<b)
print(a<=b)


a=10
b=10
print(a!=b)



# area of rectangle
length=10
breadth=5
area=length*breadth
print(area)

# area of a circle
p=3.8
r=10
area=r*r*p
print(area)


# area of a triangle
b=10
h=68
area=0.5*b*h
print(area)



a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)
print(a is not b)


a=10
b=10
print(a==b)

a=10,20
b=10,20
print(a is b)


a=10
print(a)
print(type(a))


a=2.3
print(type(a))

a=2+2j
b=7+3j

print(type(a+b))
print(a+b)


x=5>7
print(x)
print(type(x))

a=None
print(a)
print(type(a))



l=[1,2,3,45,5]
l[1]=5
print(l)
print(type(l))


t=(1,2,3,4,56,0)
t[1]=3
print(t)
print(type(t))