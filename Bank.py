Admin_Details = {}
Customer_Details = {}
Balance=0




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Admin Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===== Admin NIC check Function =====

def NIC_Admin(NIC):
    if len(NIC) == 12 and NIC.isdigit():
        if NIC in Admin_Details:
            print("This NIC is already registered.")
            return False
        return True
    else:
        print("Please enter a valid 12-digit NIC number.")
        return False


#===== Password Check Function =====
def Password(User_Password):
    if len(User_Password) == 5 and User_Password.isdigit():
        return True 
    else:
        print("Please Create Your 5 Digit Password:")
        return False 


#===== Admin User Name Craete =====
def admin_user_name(Admin_User_Name):
    global Admin_User_Name 
    global Admin_Details 
    if Admin_User_Name not in Admin_Details:
        pass
    else:
        print("Almost your User Name input")
        return Admin_User_Name





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Customer Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#================ Customer NIC check Function =================
def NIC_Customer(NIC): 
    global NIC   
    if len(NIC) == 12 and NIC.isdigit():
        if NIC not in Customer_Details:
            pass
        else:
            print("Almost your NIC input")  
            return NIC


# ============== Deposite Initialamount Function ==============
def inital_deposit(amount):
    global Balance 
    if Initial_amount >= 1000:
        Balance += Initial_amount
        print(f"Your Balance is:Rs.{Balance}")

    else:
        print("Above ammount 1000")
        return Balance
    return Initial_amount



#================ Withdraw Function =================
def Withdraw_Money(withdraw):
    global balance 
    if Withdraw <= Balance: 
        Balance -= Withdraw
        print(f"Balance is:Rs.{Balance}")
        print()

    else:
        print("Your amount not able to.Please try again")
        print()


#=============== Deposit Function ===============
def Deposit_Money(deposit):
    global Balance 
    Balance += Deposit
    print(f"Balance is:Rs.{Balance}")
    print()





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Sign up and Sign in Function +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Login_System():     
    print("Hello sir/meadam.")
    print("1.SIGN UP")               #=====New Account Admin/Customer create=====
    print("2.SIGN IN")               #=====Alredy create Admin/Customer account=====
    print("3.Exit")
    print()




#====================================================================================================================================================================================
#==========================================================================   Admin System   ========================================================================================
#====================================================================================================================================================================================

def Admin():
    while True:
        try:
            Login_System()

            select = int(input("Enter The Number:"))  

            if select == 1:
                Full_Name = input("Enter Your Full Name:")


#===== Admin NIC check Function =====
                NIC = input("Enter Your NIC Number:")
                NIC_Admin(NIC)


#===== Admin User Name Craete =====
                print()
                Admin_User_Name = input("Create Your User Name:")
                admin_user_name(Admin_User_Name)
                


#===== Password Create =====
                User_Password = input("Please Create Your 5 Digit Password:")
                Password(User_Password)

                print(f"{Full_Name} Your Admin Account Successful Create.")
                print()


                Admin_Details[NIC] =  {"Full_Name":Full_Name,"User_Name":Admin_User_Name,"user_password":User_Password}


#===== Admin Details Save Function =====
                def Save_Admin_Details(Admin_Details):
                    with open("Admin_Details","a") as Admin:
                        Admin.write(f"{Full_Name} \t {NIC} \t {Admin_User_Name} \t {User_Password} \n")

                Save_Admin_Details(Admin_Details)
                continue


#===== Admin User_Name and Password Check =====
            elif select == 2:
               NIC = input("Enter your NIC: ")
               if NIC not in Admin_Details:
                    print("NIC not found.")
                    continue


                User_Name = input("Enter your username: ")
                Password_Input = input("Enter your password: ")
                
                admin = Admin_Details[NIC]
                if admin['User_Name'] == User_Name and admin['user_password'] == Password_Input:
                    print("Login successful!")
                else:
                    print("Incorrect username or password.")
                    continue


            if select == 3:
                exit()


#==================== Menu ========================
            print()
            while True:
                print("=== Admin Menu ===")
                print("1.Create Customer Account")
                print("2.Customer Details")
                print("3.Exit")
                print()

                select = int(input("Enter The Number:"))

                if select == 1:
                    Customer_Full_Name = str(input("Enter Customer Full Name:"))

#===== Customer NIC check =====
                    NIC = input("Enter Customer NIC Number:")
                    NIC_Customer()

                    Address = input("Enter Your Address:")
                    Age = int(input("Enter Your Age:"))
                    

#===== Must Deposit ammount(>1000) =====  
                Initial_amount = int(input("Enter The Ammount:RS."))
                inital_deposit(Initial_amount)


#===== Auto creat Account Number ======
                import random
                def account_number():
                    global Customer_Details
                    global acc_num
                    acc_num = random.randint(00000000,99999999)
                    if acc_num not in Customer_Details:
                        print()
                        print(f"Hello {Customer_Full_Name}.Your Accoun Number is {acc_num}")
                        print()
                        return acc_num
                        
                account_number()    
                
                Customer_Details[NIC] = {"NIC": {"Name":Customer_Full_Name,"NIC":NIC,"Address":Address,"Age":Age,"Account_Number":acc_num ,"User_Password":User_Password}}  #User_Name:Customer_User_Name


#========= Customer Details Save =============
                with open("Customer_Details","a") as Admin:
                    Admin.write(f"{Full_Name} \t {NIC} \t {User_Password} \t {acc_num} \t {Address} \n")



#================ Admin Check Customer Details ====================
                if select == 2:
                    print(Customer_Details)

                if select == 3:
                    print("Exiting the program.Thank you!")
                    break
                

        except ValueError:
            print("Enter Number Only!")






#=====================================================================================================================================================================================          
#=========================================================================   Customer System   =======================================================================================
#=====================================================================================================================================================================================

def Customer_System():
    try:
        while True:
            Login_System()

            choose = int(input("Enter The Number:"))

            if choose == 1:
                Account_Number=int(input("Enter Your Account Number:"))
                Full_Name = input("Enter Your Full Name:")

                NIC = input("Enter Your NIC Number:")
                NIC_Customer(NIC)

        #===== Create Customer User Name =====
            print()
            Customer_User_Name = input("Create Your User Name:")
            if Customer_User_Name not in Customer_Details:
                pass
            else:
                print("Try again")

        #===== Create Customer User Password =====
            User_Password = input("Please Create Your 5 Digit Password:")
            Password(User_Password)

            print(f"{Full_Name} Your Customer Account Successful Create.")
            print()

            if choose == 2:
                User_Name = input("Enter Your User Name:")
                if Customer_Details[NIC]["User_Name"] == User_Name:
                    pass
                else:
                    print("Please Enter Your Correct User name.")


                User_Password = int(input("Enter Your Password:"))
                if Admin_Details[NIC]["user_password"] == User_Password:
                    pass
                else:
                    print("Please Enter Your Correct Password.")


            while True:
                print("1.Check Balance")
                print("2.Withdraw Money")
                print("3.Deposit Money")
                print("4.Transfer Money")
                print("5.View Accounts")
                print("6.Exit")
                

                choose=int(input("Enter (1-4): "))

                if choose==1:
                    print(f"Balance is:Rs.{Balance}")
                    print()

                elif choose==2: 
                    Withdraw = int(input("Enter Your Amount:Rs."))
                    Withdraw_Money()

                elif choose==3:  
                    Deposit = int(input("Enter Your Amount:Rs."))
                    Deposit_Money()

                elif choose == 5:
                    Input_NIC=input("Enter Your NIC:")
                    def NIC_Admin(NIC:str):
                        if len(NIC) == 12 and NIC.isdigit():
                            if NIC in Customer_Details:
                                pass
                            
                        else:
                            print("Plese Enter Your Correct NIC Number.")
                    NIC_Customer(NIC)

                elif choose==6:
                    exit()

    except ValueError:
            print("Enter Number Only!")




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 1st Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Login_Admin_User = {"Admin" : "12345"}
Login_Customer_User = {"Customer" : "12345"}




#=============== Login Function ===============
def Login():
    Input_Login_User_Name = input("Enter The Login User Name:")
    Input_Login_User_Password = input("Enter The Login User Password:")



    if Input_Login_User_Name in Login_Admin_User :
        if Login_Admin_User [Input_Login_User_Name] == Input_Login_User_Password:
            print("Welcom Admin.")
            print()
            Admin()
            return True
        else:
            print("Please Try Again. Incorrect Password.")
            return False
            


    elif Input_Login_User_Name in Login_Customer_User :
        if Login_Customer_User [Input_Login_User_Name] == Input_Login_User_Password:
            print("Welcom Customer.")
            print()
            Customer_System()
            return True
        else:
            print("Please Try Again. Incorrect Password.")
            return False

    else:
        print("Please Try Again. Incorrect User Name.")
        print()
        return False



while True:
    Login()
    break
