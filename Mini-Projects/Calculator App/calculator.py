print("Welcome to the Calculator 1.0.")
print("You can pick any of the choices specified below ")
print("For Addition:  +")
print("For Subtraction:  -")
print("For Multiplication:  *")
print("For Division:  /")
while True:
    a=float(input("Enter the first number : "))
    print("")
    b=float(input("Enter the second number : "))
    print("")
    choice=input("Enter your choice : ")
    match choice:
        case '+':
            print("Addition (+) ",a+b)
            print("")
        case '-':
            if a>b:
                print("Subtraction (-) ",a-b)
                print("")
            else:
                print("Subtraction (-) ",b-a)
                print("")
        case '*':
            print("Multiplication (*) ",a*b)
            print("")
        case '/':
            if a>b:
                print("Division (/) ",a/b)
                print("")
            else:
                print("Division (/) ",b/a)
                print("")
        case default:
            print("Please check the choice you entered.")
            print("")
            break