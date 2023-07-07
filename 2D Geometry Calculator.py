import math

def circle_area(radius):
    area = math.pi * radius ** 2
    print("Area of the circle:", area)

def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    print("Circumference of the circle:", circumference)

def square_area(side):
    area = side ** 2
    print("Area of the square:", area)

def square_perimeter(side):
    perimeter = 4 * side
    print("Perimeter of the square:", perimeter)

def rectangle_area(length, breadth):
    area = length * breadth
    print("Area of the rectangle:", area)

def rectangle_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    print("Perimeter of the rectangle:", perimeter)

def triangle_area(base, height):
    area = (base * height) / 2
    print("Area of the triangle:", area)

def triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    print("Perimeter of the triangle:", perimeter)

while True:
    print("             ")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        while True:
            print("         ")
            print("1. Area")
            print("2. Circumfarence")
            print("0. Go Back")

            choice2 = int(input("Enter Choice: "))

            if choice2==1:
                radius = float(input("Enter the radius of the circle: "))
                circle_area(radius)

            elif choice2==2:
                radius = float(input("Enter the radius of the circle: "))
                circle_circumference(radius)

            elif choice2==0:
                break

            else:
                print("Invalid Choice")
                continue
    elif choice==2:
        while True:
            print("        ")
            print("1. Area")
            print("2. Perimeter")
            print("0. Go Back")
            choice2 = int(input("Enter Choice: "))
            if choice2==1:
                side = float(input("Enter the Length of side : "))
                square_area(side)

            elif choice2==2:
                radius = float(input("Enter the Length of side: "))
                square_perimeter(side)

            elif choice2==0:
                break

        else:
            print("Invalid Choice")
            continue
    
    elif choice==3:
        while True:
            print("        ")
            print("1. Area")
            print("2. Perimeter")
            print("0. Go Back")
            choice2 = int(input("Enter Choice: "))
            if choice2==1:
                length = float(input("Enter the LENGTH of Rectangle : "))
                breadth = float(input("Enter the BREADTH of Rectangle : "))
                rectangle_area(length, breadth)

            elif choice2==2:
                length = float(input("Enter the LENGTH of Rectangle : "))
                breadth = float(input("Enter the BREADTH of Rectangle : "))
                rectangle_perimeter(length, breadth)

            elif choice2==0:
                break

            else:
                print("Invalid Choice")
                continue
            
    elif choice==4:
        while True:
            print("       ")
            print("1. Area")
            print("2. Perimeter")
            print("0. Go Back")
            choice2 = int(input("Enter Choice: "))
            if choice2==1:
                length = float(input("Enter the BASE of Triangle : "))
                breadth = float(input("Enter the HEIGHT of Triangle : "))
                triangle_area(base, height)

            elif choice2==2:
                side1 = float(input("Enter the SIDE1 of Rectangle : "))
                side2 = float(input("Enter the SIDE2 of Rectangle : "))
                side3 = float(input("Enter the SIDE3 of Rectangle : "))
                triangle_perimeter(side1, side2, side3)

            elif choice2==0:
                break

            else:
                print("Invalid Choice")
                continue
    
    elif choice==0:
        break

    else:
        print("Invalid Choice")
        continue

print("Thanks for using GEOMETRY CALCULATOR")
