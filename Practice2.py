while True :
    
    print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n")
    
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))

    Choice=int(input("Enter your Choice : "))
    
    if Choice==1:
        print(num1+num2)
        print('--------')
    elif Choice==2:
        print(num1-num2)
        print('--------')
    elif Choice==3:
        print(num1*num2)
        print('--------')
    elif Choice==4:
        print(num1/num2)
        print('--------')
    else:
        exit 