def addition(num1,num2):
    sum=num1+num2
    print(sum)

def subtract(num1,num2):
    sub=num1-num2
    print(sub)

def multiply(num1,num2):
    mul=num1*num2
    print(mul)

def divide(num1,num2):
    div=num1/num2
    print(div)

def square(num1):
    print(num1*num1)



In1=int(input("Enter first number: "))
In2=int(input("Enter second number: "))

while True:
    choice=int(input("Enter Choice: "))

    if choice==1:
        addition(In1,In2)
    elif choice==2:
        subtract(In1,In2)
    elif choice==3:
        multiply(In1,In2)
    elif choice==4:
        divide(In1,In2)
    elif choice==5:
        square(In1)
        square(In2)
    else:
        break


print('Thanks') 