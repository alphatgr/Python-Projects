print("Welcome to the Calculator 1.0. \n")
print("You can pick any of the choices specified below \n")
print("For Addition:  + \n")
print("For Subtraction:  - \n")
print("For Multiplication:  * \n")
print("For Division:  / \n")
print("")
while True:
    a=float(input("Enter the first number : \n"))
    b=float(input("Enter the second number : \n"))
    choice=input("Enter your choice : \n")
    print("")
    match choice:
        case '+':
            print("Addition (+) ",a+b,"\n")
        case '-':
            if a>b:
                print("Subtraction (-) ",a-b,"\n")
            else:
                print("Subtraction (-) ",b-a,"\n")
        case '*':
            print("Multiplication (*) ",a*b,"\n")
        case '/':
            if a>b:
                print("Division (/) ",a/b,"\n")
            else:
                print("Division (/) ",b/a,"\n")
        case default:
            print("Please check the choice you entered. \n")
            break