#This function checks if the user input is indeed a numbe
def check_numbers():

    while True:
        try:
            number = float(input("Enter a number\n"))
            return(number)
            break
        except ValueError:
            print('You did not enter a number. Please enter a number')
#This function checks if the user input for the operation is either +, -, *, /
def check_operation(op, a, b):
    if op == '+':
        return (a + b)
        print(a + b)
    elif op == '-':
        return (a - b)
        print(a - b)
    elif op == '*':
        return (a * b)
        print(a * b)
    elif op == '/':
        return (a / b)
        print(a / b)
    elif op == '=':
        return (a)
        print(a)
    else:
        print('you did not enter a correct operation')
        return(a)


#initializing op for the while loop to work
op = 1
a = check_numbers()

while op != "=":
    op = input("Enter the operation\n")
    #This if statement allows us to exit the loop without asking the user to give another number after he typed =
    if op != '=':
        b = check_numbers()
    a = check_operation(op, a, b)
    print('your result is')
    print(a)






