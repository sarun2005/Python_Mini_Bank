Admin_Details={}
User_Account_Details={}
Balance=0

#=====Login system=====
while True:
    try:
        print("Hello sir/meadam.")
        print("1.SIGN UP")               #=====New Account create=====
        print("2.SIGN IN")               #=====Alredy create account=====
        select=int(input("Enter The Number:"))    

#=====Creat Account Details=====
        if select==1:
            Full_Name=str(input("Enter Your Full Name:"))

#=====NIC check=====
            NIC=int(input("Enter Your NIC Number:"))
            if NIC==12:
                pass
            else:
                print("Please Enter Your 12 Digit NIC number.")

            Address=input("Enter Your Address:")
            Age=int(input("Enter Your Age:"))

#=====Password Create=====
            User_Password=int(input("Please Create Your 5 Digit Password:"))
            if User_Password==5:
                print()
            else:
                print("Try again.")
            

#=====Must Deposit ammount(>1000)=====  
            ammount=int(input("Enter The Ammount:RS."))

        def deposit():
            if ammount>=1000:
                Balance+=ammount
                print(f"Your Balance is:Rs.{Balance}")

            else:
                print("Above ammount 1000")
          
#=====Auto creat Account Number======
        import random
        def account_number():
            global User_Account_Details
            acc_num=random.randint(0000000000,9999999999)
            if acc_num not in User_Account_Details:
                print(f"Hello {Full_Name}.Your Accoun Number is {acc_num}")
       
        account_number()    
        
        
        User_Account_Details={"Name":Full_Name,"NIC":NIC,"Address":Address,"Age":Age}
        print(User_Account_Details)


        if select==2:
            Account_Number=int(input("Enter Your Accoun Number:"))
            Password=int(input("Enter Your Password:"))
            print()
            
          
    
    except ValueError:
        print("Enter Number Only!")


#=====Menu=====
"""  while True:
        print("1.Check Balance")
        print("2.Withdraw")
        print("3.Deposit")
        print("4.Transaction History")
        print("5.Exit")

        choose=int(input("Enter (1-4): "))    

#=====Balance check=====
        if choose==1:
            print(f"Balance is:Rs.{Balance}")
            print()

#=====Withdraw=====
        elif choose==2: 
            Withdraw=int(input("Enter your amount:Rs."))
            
            if Withdraw<=Balance: 
                Balance=Balance-Withdraw
                print(f"Balance is:Rs.{Balance}")
                print()

            else:
                print("Your amount not able to.Please try again")
                print()

#=====Deposit=====
        elif choose==3:  
            Deposit=int(input("Enter your amount:Rs."))
            Balance=Deposit+Balance
            print(f"Balance is:Rs.{Balance}")
            print()
            
#=====Transaction History=====



#=====Exiting Program=====
        elif choose==5:
            exit()


    """



"""#===== Password Create =====
            User_Password=int(input("Please Create Your 5 Digit Password:"))"""


"""#===== Exit Programe =====
            def Exit_Programe():
                if select==3:
                    print("Exiting the program.Thank you!")
                    
            Exit_Programe()"""

''''print()
def Exit_Programe():
    print("Exiting the program.Thank you!")'''

#===== Exit Programe =====
""" if select==3:  
                Exit_Programe()
                break
"""