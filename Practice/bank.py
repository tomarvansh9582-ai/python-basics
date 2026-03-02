import time
print("\t\t\t\tWELCOME TO BANK SYSTEM")
for a in range(1,101):
    print("*",end="")
    time.sleep(.1)
NAME=str(input("\n\t\t\tENTER YOUR NAME"))
print("\t\t\tWELCOME USER",NAME)
balance=90000
npass=12345
password=int(input("\t\tenter your password"))
if password!=npass:
    print("WRONG PASSWORD TRY AGAIN")
else:
      n=5
      while n==5:
             print("\t\t\t\tWELCOME USER TO THE BANKING MENU")
             for a in range(1,101):
                 print("*",end="")
                 time.sleep(.1)
             print("\nENTER 1 FOR DEPOSIT\nENTER 2 FOR CHECKING BANK BALANCE\nENTER 3 FOR WITHDRAWL\nENTER 4 EXIT\nENTER 5 FOR MAIN MENU")
             n=int(input("ENTER YOU CHOICE"))
             if n==1: 
                print("\t\tINTIAL BALANCE=\t",balance)
                deposit=int(input("\t\tENTER THE MONEY TO DEPOSIT"))
                balance=balance+deposit
                print("\t\tFINAL BALANCE=",balance)
                print("\t\t THANK YOU USER",NAME) 
             if n==2:
                print("\t\tYOUR BALANCE IS",balance)
                print("\t\t THANK YOU USER",NAME) 
             if n==3:
                print("\t\tINTIAL BALANCE=\t",balance)
                withdraw=int(input("\t\tENTER THE MONEY TO WITHDRAW"))
                balance=balance-withdraw
                print("\t\tFINAL BALANCE=",balance)
                print("\t\t THANK YOU USER",NAME)
             if n==4:
                 break
             print("\n\n\n\t\tdo you want to continue")
             print("enter the y/n")
             choice=str(input("enter your choice"))
             if choice=='y' or choice=='Y':
                 n=5
             else:
                 balance=0
                 break;
