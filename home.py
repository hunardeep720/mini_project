import re
user_new_password = ""
user_confirm_password = ""
user_new_email = ""
def validate_passsword(user_new_password,user_confirm_password,user_new_email):
    if user_new_password == user_confirm_password:
            if len(user_new_password) >= 8:
                validate_email = re.search("(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$",user_new_password)
                if validate_email != None:
                    print("Welcome to our website")
                    with open("emails_passwords.txt",mode="a") as add_email:
                        add_email.write(f'\n{user_new_email} {user_new_password}')
                else :
                    print("Enter the password using special characters, uppercase leters, lowercase letters, numbers() and it should be atleast 8 characters")
                    sign_up()
            else:
                 print("Enter the password containig atleast 8 characters")
                 sign_up()
    else:
         print("Given password and confirm password is different")
         sign_up()
                
                       
def sign_in(sign):
        count = 0
        loop = True
        while loop == True:
            count+=1
            if count == 4:
                print("Sorry try again!\nIf you are new, please sign up")
                loop = False
                break
            elif count > 1:
                print(f'You have { 4- count} tries')
                print
            user_exist_email = input("Enter your email\n")
            user_exist_password = input("Enter your password\n")
            user_list = list()
            user_list.append(user_exist_email)
            user_list.append(user_exist_password)
            with open("emails_passwords.txt", mode="r") as check_email:
                for data in check_email:    
                    data_strip = data.strip("\n")
                    arrange_data = data_strip.split(" ")
                    if user_list == arrange_data:
                        print("Welcome to program")
                        loop = False
                        break
                    elif user_list != arrange_data:
                        continue  

def sign_up():
        user_new_email = input("Enter your email\n")
        user_new_password = input("Enter your new password\n")
        user_confirm_password = input("Confirm new password\n")
        validate_passsword(user_new_password,user_confirm_password,user_new_email)
        
                        
def display_menu():
    sign = input("Enter '1' for sign in or '2' for sign up\n")
    if sign == '1':
        sign_in(sign)
    elif sign == '2':
        sign_up()                 
    else:
        print("Invalid input")
display_menu()
