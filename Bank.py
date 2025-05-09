Admin_Details = {}
Customer_Details = {}
Balance = 0



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Admin Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ==================== Admin NIC check Function ====================
def NIC_Admin(NIC):
    for i  in range(3):
        if len(NIC) == 12 and NIC.isdigit():
            if NIC not in Admin_Details:
                return True
            else:
                print("This NIC is already registered.")
                return False
                    
        else:
            print("Please Enter a Valid 12-Digit NIC number.")
            print()
        return False

    
                
# ==================== Admin User Name Create Function ====================
def admin_user_name(Admin_User_Name):
    if Admin_User_Name not in Admin_Details:
        return True
    else:
        print("This User Name is already registered.")
        return False



# ==================== Admin User Password Create Function ====================
def Password(User_Password):
    if len(User_Password) == 5 and User_Password.isdigit():
        return True
    else:
        print("Please Enter a Valid 5-Digit Password Number.")
        return False
    


# ==================== Phone Number Function ====================
def phone_number(Phone_Number):
    for i  in range(3):
        if len(Phone_Number) == 10 and Phone_Number.isdigit():
            return True
        else:
            print("Please Enter a Valid 10-Digit Phone Number.")
            print()     
    return False
    
    



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Customer Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ==================== Customer NIC check Function ====================
def NIC_Customer(NIC):
    if len(NIC) == 12 and NIC.isdigit():
        if NIC in Customer_Details:
            print("This NIC is already registered.")
            return False
        return True
    else:
        print("Please enter a valid 12-digit NIC number.")
        return False
    


# ==================== Phone Number Function ====================
def customer_phone_number(Customer_Phone_Number):
    for i  in range(3):
        if len(Customer_Phone_Number) == 10 and Customer_Phone_Number.isdigit():
            return True
        else:
            print("Please Enter a Valid 10-Digit Phone Number.")
            print()     
    return False
    



# ==================== Customer User Name Create Function ====================
def customer_user_name(Customer_User_Name):
    global Customer_Details
    if Customer_User_Name not in Customer_Details:
        return True
    else:  
        print("This User Name is already registered.")
        return False 



# ==================== Admin User Password Create Function ====================
def Customer_Password(Customer_User_Password):
    if len(Customer_User_Password) == 5 and Customer_User_Password.isdigit():
        return True
    else:
        print("Please Create Your 5 Digit Password:")
        return False



# ==================== Deposit Initial Amount Function ====================
def inital_deposit(Initial_amount):
    global Balance
    if Initial_amount >= 1000:
        Balance += Initial_amount
        print(f"Initial Amount Successful Deposit. Your Balance is:Rs.{Balance}")
        return Balance
    else:  
        print("Your Amount Must be Over Rs.1000.")
        return False




# ==================== Withdraw Function ====================
def Withdraw_Money(Withdraw_Amount):
    global Balance
    if Withdraw_Amount <= Balance:
        Balance -= Withdraw_Amount
        print(f"Withdraw Successful. Your Balance is:Rs.{Balance}")
        print()
        return True
    else:  
        print("Insufficient balance. Please try again")  
        print()
        return False



# ==================== Deposit Function ====================
def Deposit_Money(Deposit_Amount):
    global Balance
    Balance += Deposit_Amount
    print(f"Deposit successful. Your Balance is: Rs.{Balance}")
    return True


#  ==================== Amount Transfer Function ====================
def Transfer_Money():
    Sender_NIC = input("Please Enter Your NIC:").strip() 
    Sender_Account_Number = int(input("Please Enter Your Account Number:")).strip()
    if Sender_NIC not in Customer_Details and Customer_Details[Sender_NIC]["Account_Number"] != Sender_Account_Number  :
        print("Sender Account not Found.")
        return



    Receiver_NIC = input("Please Enter Receiver NIC:").strip()
    Receiver_Account_Number =  int(input("Please Enter Receiver Account Number:")).strip()
    if Receiver_NIC not in Customer_Details and Customer_Details[Receiver_NIC]["Account_Number"] != Receiver_Account_Number :
        print("Receiver Account not Found.")
        return



    amount = int(input("Enter Amount to Transfer: Rs. "))

    if amount >= 100 :
        if Customer_Details[Sender_NIC]["Balance"] >= amount:
            Customer_Details[Sender_NIC]["Balance"] -= amount
            Customer_Details[Receiver_NIC ]["Balance"] += amount

            print(f"Transfer Successful! Rs.{amount} sent to {Customer_Details[Receiver_NIC ]['Name']}")
            print(f"Your Updated Balance: Rs.{Customer_Details[Sender_NIC]['Balance']}")
        else:
            print("Your Amount above your balance.")
    else:
        print("Amount should be above 100.")
        return




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

# ==================== Admin NIC check Function ====================
                NIC = input("Enter Your NIC Number:").strip()
                if NIC_Admin(NIC) == False:
                    print("Too Many Invalid Attampts. Exiting Programe.....")
                    break
                

                Admin_Address = input("Enter Your Address:")



# ==================== Phone Number  ====================
                Phone_Number = input("Enter Your Phone Number:")
                if phone_number(Phone_Number) == False:
                    print("Too Many Invalid Attampts. Exiting Programe.....")
                    break



# ==================== Admin User Name Create====================
                print()
                Admin_User_Name = input("Create Your User Name:")
                admin_user_name(Admin_User_Name)



# ==================== Password Create ====================
                User_Password = input("Please Create Your 5 Digit Password:")
                Password(User_Password)
            

                print(f"{Full_Name} Your Admin Account Successful Create.")  
                print()  

                Admin_Details[NIC] = { "Full_Name": Full_Name, "NIC":NIC, "Phone_Number": Phone_Number, "Address": Admin_Address, "Admin_User_Name":Admin_User_Name, "User_Password":User_Password}



# ==================== Admin Details Save ====================
                with open("Admin_Details.txt", "a") as Admin_file:
                    Admin_file.write(f"{Full_Name} |\t {NIC} |\t {Admin_Address} |\t {Phone_Number} \n")



# ==================== Admin User Name and Password Save  ====================
                with open("Admin_User_Name_and_Password .txt", "a") as Admin_file:
                    Admin_file.write(f" {NIC} |\t {Admin_User_Name} |\t {User_Password} \n")

                continue



#==================== Admin User_Name and Password Check ====================
            elif select == 2:
                NIC = input("Please Enter your NIC:").strip()
                User_Name = input("Enter Your User Name:") 
                User_Password = input("Enter Your Password:")   

                if NIC in Admin_Details:
                    if Admin_Details[NIC]["Admin_User_Name"] !=User_Name and Admin_Details[NIC]["User_Password"] != User_Password:  
                        print("Please Enter Your Correct User Name and User Password.")  

                else:
                    print("Your NIC not found.")



# ==================== Menu ====================
                print()
                while True:
                    print("=== Admin Menu ===")
                    print("1.Create Customer Account")
                    print("2.Customer Details")
                    print("3. Update Customer Details")
                    print("4.Exit")
                    print()

                    select = int(input("Please Select The Number:"))  

                    if select == 1:  
                        Customer_Full_Name = str(input("Enter Customer Full Name:"))
                        

# ==================== Phone Number  ====================
                        Customer_Phone_Number = input("Enter Your Phone Number:")
                        if customer_phone_number(Customer_Phone_Number) == False:
                            print("Too Many Invalid Attampts. Exiting Programe.....")
                            break



# ==================== Customer NIC Check =====================
                        NIC = input("Enter Customer NIC Number:").strip()
                    

                        Address = input("Enter Your Address:")  
                        Age = int(input("Enter Your Age:"))



# ====================== Must Deposit amount(>1000) ===================
                        Initial_amount = int(input("Enter The Amount:RS."))
                        inital_deposit(Initial_amount)



# ==================== Auto create Account Number ====================
                        import random
                        def account_number():
                            acc_num = random.randint(00000000, 99999999)
                            if acc_num not in Customer_Details:
                                print()
                                print(f"Hello {Customer_Full_Name}. Your Account Number is {acc_num}")
                                print()
                                return acc_num
                            return account_number()

                        acc_num = account_number()      




# ==================== Customer Details Save ====================
                        with open("Customer_Details.txt", "a") as Customer_file:
                            Customer_file.write(f"{Customer_Full_Name} |\t {NIC}  |\t {acc_num} |\t {Address} |\t {Age} |\t {Balance} |\t {Customer_Phone_Number} \n")



                        Customer_Details[NIC] = { "Name": Customer_Full_Name, "NIC":NIC, "Address": Address, "Age": Age, "Account_Number":acc_num, "Phone_Number":Customer_Phone_Number,  "Balance": Balance }
                       

# ==================== Admin Check Customer Details ====================

                    elif select == 2:
                        NIC = input("Enter Customer NIC to View Details:").strip()
                        if NIC in Customer_Details:
                            print()
                            print(f"==== {NIC} Customer Details ====")
                            print(f"Full Name: {Customer_Details[NIC]['Name']}")
                            print(f"Address: {Customer_Details[NIC]['Address']}")
                            print(f"Age: {Customer_Details[NIC]['Age']}")
                            print(f"Account Number: {Customer_Details[NIC]['Account_Number']}")
                            print(f"Balance: Rs.{Customer_Details[NIC]['Balance']}")
                            print()
                        else:
                            print("Customer NIC not Found.")


                    elif select == 3:
                       pass


                    if select == 4:  
                        print("Thank you!. Exiting Programe...... ")
                        print()  
                        break  


            elif select == 3:
                print("Thank you!. Exiting Programe...... ")
                exit()


        except ValueError:  
            print("Enter Number Only!")




# =====================================================================================================================================================================================
# =========================================================================   Customer System   =======================================================================================
# =====================================================================================================================================================================================



def Customer_System():
    try:
        while True:
            Login_System()
            choose = int(input("Please Select The Number:"))  

            if choose == 1:  
                Account_Number = int(input("Enter Your Account Number:"))  
                Full_Name = input("Enter Your Full Name:")  

                NIC = input("Enter Your NIC Number:")  
                NIC_Customer(NIC)



# ===================== Create Customer User Name ====================  
                print()  
                Customer_User_Name = input("Create Your User Name:") 
                customer_user_name(Customer_User_Name) 



# ==================== Create Customer User Password ====================  
                Customer_User_Password = input("Please Create Your 5 Digit Password:")  
                Customer_Password(Customer_User_Password)

                print(f"{Full_Name} Your Customer Account Successful Create.")  
                print()  

                Customer_Details[NIC] = {"NIC": NIC, "User_Name":Customer_User_Name, "User_Password": Customer_User_Password}



# ==================== Customer User Name and Password Save ====================
                with open("Customer_User_Name_and_Password.txt", "a") as Customer_file:
                    Customer_file.write(f"{NIC} |\t {Customer_User_Name} |\t {Customer_User_Password} \n")



            elif choose == 2:  
                NIC = input("Enter Your NIC:")
                User_Name = input("Enter Your User Name:") 
                User_Password = input("Enter Your Password:") 


                if NIC in Customer_Details:
                    if Customer_Details[NIC]["User_Name"] !=User_Name and Customer_Details[NIC]["User_Password"] != User_Password:  
                        print("Please Enter Your Correct User Name and User Password.")  

                else:
                    print("Your NIC not found.")    



                while True: 
                    print() 
                    print("1.Check Balance")  
                    print("2.Withdraw Money")  
                    print("3.Deposit Money")  
                    print("4.Transfer Money")  
                    print("5.View Accounts")  
                    print("6.Exit") 
                    print() 


                    choose = int(input("Please Select The Number:"))  



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
                        Transfer_Money()

                    elif choose == 5:  
                        Input_NIC = input("Enter Your NIC:").strip()  
                        if Input_NIC in Customer_Details:  
                            print(Customer_Details[Input_NIC])  
                        else:  
                            print("Please Enter Your Correct NIC Number.")  

                    elif choose == 6:  
                        break  

            elif choose == 3:
                break

    except ValueError:  
        print("Enter Number Only! ")



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 1st Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Login_Admin_User = {"Admin": "12345"}
Login_Customer_User = {"Customer": "12345"}


# =============== Login Function ===============
def Login():
    while True:
        Input_Login_User_Name = input("Enter The Login User Name: ")
        Input_Login_User_Password = input("Enter The Login User Password: ").strip()


        if Input_Login_User_Name in Login_Admin_User:  
            if Login_Admin_User[Input_Login_User_Name] == Input_Login_User_Password:  
                print("Welcome Admin.")  
                print()  
                Admin()  
                return True 
            else:  
                print("Please Try Again. Incorrect User Password.")
                print()  



        elif Input_Login_User_Name in Login_Customer_User:  
            if Login_Customer_User[Input_Login_User_Name] == Input_Login_User_Password:  
                print("Welcome Customer.")  
                print()  
                Customer_System()  
                return True  
            else:  
                print("Please Try Again. Incorrect User Password.") 
                print() 


        else:  
            print("Please Try Again. Incorrect User Name.")  
            print()  


Login()