# ====== Amount Transfer=========
def Transfer_Money():
    Sender_NIC = input("Please Enter Your NIC:") 
    Sender_Account_Number = int(input("Please Enter Your Account Number:"))
    if Sender_NIC not in Customer_Details and Sender_Account_Number not in Customer_Details :
        print("Sender Account not Found.")
        return



    Receiver_NIC = input("Please Enter Receiver NIC:")
    Receiver_Account_Number =  int(input("Please Enter Receiver Account Number:"))
    if Receiver_NIC not in Customer_Details and Receiver_Account_Number not in Customer_Details :
        print("Receiver Account not Found.")
        return



    amount = int(input("Enter Amount to Transfer: Rs. "))
    if amount >= 100 :
        pass
    else:
        print("Amount should be above 100.")
        return



    if Customer_Details[Sender_NIC]["Balance"] >= amount:
        Customer_Details[Sender_NIC]["Balance"] -= amount
        Customer_Details[Receiver_NIC ]["Balance"] += amount


        print(f"Transfer Successful! Rs.{amount} sent to {Customer_Details[Receiver_NIC ]['Name']}")
        print(f"Your Updated Balance: Rs.{Customer_Details[Sender_NIC]['Balance']}")
    else:
        print("")


#======== Update Custemer Details =========
 Update_NIC = input("Enter Customer NIC to Update: ")
                        if Update_NIC in Customer_Details:
                            print("What would you like to update?")
                            print("1. Address")
                            print("2. Age")
                            print("3. Name")
        
                            Option = input("Select Option (1-3): ")

                            if Option == "1":
                                new_address = input("Enter Customer New Address: ")
                                Customer_Details[Update_NIC]["Address"] = new_address
                                print("Address updated successfully.")
                                
                                
                            elif Option == "2":
                                new_age = input("Enter new Age: ")
                                Customer_Details[Update_NIC]["Age"] = int(new_age)
                                print("Age updated successfully.")
                                
                                
                            elif Option == "3":
                                new_name = input("Enter new Full Name: ")
                                Customer_Details[Update_NIC]["Name"] = new_name
                                print("Name updated successfully.")
        
                            else:
                                 print("Invalid Option.")

                                  else:
                        print("Customer NIC not found.")

    
# ========== login =====

        """ if Input_Login_User_Name in Login_Admin_User or Input_Login_User_Name in Login_Customer_User :       
            if Login_Admin_User[Input_Login_User_Name] != Input_Login_User_Password and Login_Customer_User[Input_Login_User_Name] != Input_Login_User_Password:
                print("Please Try Again. Incorrect User Name and User Password.")
                """