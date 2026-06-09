from storage import load
from storage import save

def account_menu():
    print("Now we can start designing the account menu...")

def main():
    while True:
        print("\n#<<--Banking System CLI-->>#")
        print(" 1. Log in to your account")
        print(" 2. Create a new account")
        print(" 3. Exit\n")

        try:
            user = int(input("Enter choice: ").strip())
        except ValueError:
            print("Invalid input! Enter numbers only.")

        if user == 1:
            data = load()
            acc_num = input("Enter account number: ").strip()
            if acc_num == "":
                print("Account number cant be empty!")
                return
        
            for user_acc_num, details in data.items():
                if acc_num == user_acc_num:                     
                    user_password = input("Enter password: ").strip()
                    if user_password != "":
                        if details['Password'] == user_password:
                            account_menu()
                        
                    else:
                        print("Password can't be empty!")
                        return
                
        elif user == 2:
            data = load()
            try:
                user_acc_num = int(input("Enter account number: ").strip())
            except ValueError:
                print("Enter numbers only!")
                
            password = input("Enter password: ").strip()
            if password != "":
                data[user_acc_num] = {
                    "Account Number": user_acc_num ,
                    "Password": password
                }

                save(data)
                print("Account created successfully")
            else:
                print("Name can't be empty!")
                
        elif user == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid input! Enter 1 to 3\n")

main()
