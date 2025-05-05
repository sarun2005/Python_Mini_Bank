Admin_Details = {}
Customer_Details = {}
Balance = 0

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Admin Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ===== Admin NIC check Function =====
def NIC_Admin(NIC):
    if len(NIC) == 12 and NIC.isdigit():
        if NIC in Admin_Details:
            print("This NIC is already registered.")
            return False
        return True
    else:
        print("Please enter a valid 12-digit NIC number.")
        return False

# ===== Password Check Function =====
def Password(User_Password):
    if len(User_Password) == 5 and User_Password.isdigit():
        return True
    else:
        print("Please Create Your 5 Digit Password:")
        return False

# ===== Admin User Name Create =====
def admin_user_name(Admin_User_Name):
    if Admin_User_Name not in Admin_Details:
        return True
    else:
        print("This User Name is already registered.")
        return False

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Customer Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ================ Customer NIC check Function =================
def NIC_Customer(NIC):
    if len(NIC) == 12 and NIC.isdigit():
        if NIC in Customer_Details:
            print("This NIC is already registered.")
            return False
        return True
    else:
        print("Please enter a valid 12-digit NIC number.")
        return False



# ============== Deposit Initial amount Function ==============
def inital_deposit(Initial_amount):
    global Balance
    if Initial_amount >= 1000:
        Balance += Initial_amount
        print(f"Initial Amount Successful Deposit. Your Balance is:Rs.{Balance}")
        return True
    else:  
        print("Your Amount Must be Over Rs.1000.")
        return False

# ================ Withdraw Function =================
def Withdraw_Money(Withdraw_Amount):
    global Balance
    if Withdraw <= Balance:
        Balance -= Withdraw_Amount
        print(f"Withdraw Successful. Your Balance is:Rs.{Balance}")
        print()
        return True
    else:  
        print("Insufficient balance. Please try again")  
        print()
        return False

# =============== Deposit Function ===============
def Deposit_Money(Deposit_Amount):
    global Balance
    Balance += Deposit_Amount
    print(f"Deposit successful. Your Balance is: Rs.{Balance}")
    return True

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Sign up and Sign in Function +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Login_System():
    print("Hello sir/madam.")
    print("1.SIGN UP")               # =====New Account Admin/Customer create=====
    print("2.SIGN IN")               # =====Already create Admin/Customer account=====
    print("3.Exit")
    print()

# ====================================================================================================================================================================================
# ==========================================================================   Admin System   ========================================================================================
# ====================================================================================================================================================================================

def Admin():
    while True:
        try:
            Login_System()
            select = int(input("Enter The Number:"))    

            if select == 1:  
                Full_Name = input("Enter Your Full Name:")

                # ===== Admin NIC check Function =====
                NIC = input("Enter Your NIC Number:")
                if not NIC_Admin(NIC):
                    continue

                # ===== Admin User Name Create =====
                print()
                Admin_User_Name = input("Create Your User Name:")
                if not admin_user_name(Admin_User_Name):
                    continue

                # ===== Password Create =====
                User_Password = input("Please Create Your 5 Digit Password:")
                if not Password(User_Password):
                    continue

                print(f"{Full_Name} Your Admin Account Successful Create.")  
                print()  

                Admin_Details[NIC] = {
                    "Full_Name": Full_Name,
                    "User_Name": Admin_User_Name,
                    "user_password": User_Password
                }

                # ===== Admin Details Save Function =====
                def Save_Admin_Details():
                    with open("Admin_Details.txt", "a") as Admin_file:
                        Admin_file.write(f"{Full_Name} \t {NIC} \t {Admin_User_Name} \t {User_Password} \n")

                Save_Admin_Details()  
                continue

            # ===== Admin User_Name and Password Check =====
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

                # ==================== Menu ========================
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

                        # ===== Customer NIC check =====
                        NIC = input("Enter Customer NIC Number:")
                        if not NIC_Customer(NIC):
                            continue

                        Address = input("Enter Your Address:")  
                        Age = int(input("Enter Your Age:"))

                        # ===== Must Deposit amount(>1000) =====
                        Initial_amount = int(input("Enter The Amount:RS."))
                        if not inital_deposit(Initial_amount):
                            continue

                        # ===== Auto create Account Number ======
                        import random
                        def account_number():
                            acc_num = random.randint(0, 99999999)
                            if acc_num not in Customer_Details:
                                print()
                                print(f"Hello {Customer_Full_Name}. Your Account Number is {acc_num}")
                                print()
                                return acc_num
                            return account_number()

                        acc_num = account_number()      
                        
                        Customer_Details[NIC] = {
                            "Name": Customer_Full_Name,
                            "NIC": NIC,
                            "Address": Address,
                            "Age": Age,
                            "Account_Number": acc_num,
                            "User_Password": User_Password,
                            "Balance": Balance
                        }

                        # ========= Customer Details Save =============
                        with open("Customer_Details.txt", "a") as Customer_file:
                            Customer_file.write(f"{Customer_Full_Name} \t {NIC} \t {User_Password} \t {acc_num} \t {Address} \n")

                    # ================ Admin Check Customer Details ====================
                    elif select == 2:
                        print(Customer_Details)

                    elif select == 3:  
                        print("Exiting the program. Thank you!")  
                        break  

            elif select == 3:
                break

        except ValueError:  
            print("Enter Number Only!")

# =====================================================================================================================================================================================
# =========================================================================   Customer System   =======================================================================================
# =====================================================================================================================================================================================

def Customer_System():
    try:
        while True:
            Login_System()
            choose = int(input("Enter The Number:"))  

            if choose == 1:  
                Account_Number = int(input("Enter Your Account Number:"))  
                Full_Name = input("Enter Your Full Name:")  

                NIC = input("Enter Your NIC Number:")  
                if not NIC_Customer(NIC):
                    continue

                # ===== Create Customer User Name =====  
                print()  
                Customer_User_Name = input("Create Your User Name:")  
                if Customer_User_Name in Customer_Details:  
                    print("User Name already exists. Try again")  
                    continue

                # ===== Create Customer User Password =====  
                User_Password = input("Please Create Your 5 Digit Password:")  
                if not Password(User_Password):
                    continue

                print(f"{Full_Name} Your Customer Account Successful Create.")  
                print()  

            elif choose == 2:  
                User_Name = input("Enter Your User Name:")  
                NIC = input("Enter Your NIC:")  
                
                if NIC not in Customer_Details or Customer_Details[NIC]["User_Name"] != User_Name:  
                    print("Please Enter Your Correct User name.")  
                    continue

                User_Password = input("Enter Your Password:")  
                if Customer_Details[NIC]["User_Password"] != User_Password:  
                    print("Please Enter Your Correct Password.")  
                    continue

                while True:  
                    print("1.Check Balance")  
                    print("2.Withdraw Money")  
                    print("3.Deposit Money")  
                    print("4.Transfer Money")  
                    print("5.View Accounts")  
                    print("6.Exit")  
                    
                    choose = int(input("Enter (1-6): "))  

                    if choose == 1:  
                        print(f"Your Balance is:Rs.{Balance}")  
                        print()  

                    elif choose == 2:   
                        Withdraw_Amount = int(input("Enter Your Amount:Rs."))  
                        Withdraw_Money(Withdraw_Amount)  

                    elif choose == 3:    
                        Deposit_Amount = int(input("Enter Your Amount:Rs."))  
                        Deposit_Money(Deposit_Amount)  

                    elif choose == 4:  
                        pass  

                    elif choose == 5:  
                        Input_NIC = input("Enter Your NIC:")  
                        if Input_NIC in Customer_Details:  
                            print(Customer_Details[Input_NIC])  
                        else:  
                            print("Please Enter Your Correct NIC Number.")  

                    elif choose == 6:  
                        return  

            elif choose == 3:
                break

    except ValueError:  
        print("Enter Number Only! ")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 1st Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Login_Admin_User = {"Admin": "12345"}
Login_Customer_User = {"Customer": "12345"}

# =============== Login Function ===============
def Login():
    Input_Login_User_Name = input("Enter The Login User Name: ")
    Input_Login_User_Password = input("Enter The Login User Password: ")

    if Input_Login_User_Name in Login_Admin_User:  
        if Login_Admin_User[Input_Login_User_Name] == Input_Login_User_Password:  
            print("Welcome Admin.")  
            print()  
            Admin()  
            return True  
        else:  
            print("Please Try Again. Incorrect Password.")  
            return False  
          
    elif Input_Login_User_Name in Login_Customer_User:  
        if Login_Customer_User[Input_Login_User_Name] == Input_Login_User_Password:  
            print("Welcome Customer.")  
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