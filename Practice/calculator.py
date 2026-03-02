n='y'
while n=='y' or n=='Y':
    p = int(input("Enter the first input: "))
    q = int(input("Enter the second input: "))
    oper = int(input("Enter the type of operation you want to perform 1 to perform +\n2 to perform  - \n 3 to perform *\n 4 to perform  /\n 5 to perform % "))
    if oper == 1:
        result = p+q
    elif oper == 2:
        result = p-q
    elif oper == 3:
        result = p*q
    elif oper == 4:
        result = p//q # Integer Division
    elif oper == 5:
        result = p%q
    print("Your answer is: ",result)
    print("do yo want to continue")
    n=str(input("enter y/n"))
