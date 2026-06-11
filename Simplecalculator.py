num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
calculator=input("Enter the calculator  ")
if calculator == "+":
    print(num1+num2)
elif calculator=="-":
    print(num1-num2)
elif calculator=="*":
    print(num1*num2)
elif calculator=="/":
    print(num1/num2)
else:
    print("invalid proof")