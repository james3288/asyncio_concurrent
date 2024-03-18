import getpass
from accounts import User
import time
from userCredential import UserCredentials

on:bool = True
# user = User()

while on:
    
    print(fr'***Welcome to KJ ATM***')
    print("")
    print("1 - Withdraw")
    print("2 - Balance")
    print("3 - Change Password")
    print("")

    try:
        result = int(input("Enter the number you selected: \n"))
        
        if result > 3 or result <= 0:
            print('you must select either 1,2 or 3 \n')
        else:
            match result:
                case 1:              
                    user = UserCredentials()
                    user1 = user.credentials()

                    if len(user1) > 0:
                        user.remainingBalance(user1)

                        try:
                            amount = float(input("Input amount to withdraw:"))
                            print("transaction has been processed, please wait...")
                            time.sleep(5)

                            user.updateUser(amount)

                            print("successfully withdrawn.")
                            user.remainingBalance(user1)

                        except ValueError as e:
                            print('You must input a number only')
                    else:
                        print('incorrect username or password, you may try again.. \n')
                case 2:
                    user = UserCredentials()
                    user1 = user.credentials()

                    if len(user1) > 0:
                        print("\n")
                        user.remainingBalance(user1)

                case 3:
                    user = UserCredentials()
                    user1 = user.credentials()

                    if len(user1) > 0:
                        newPassword = getpass.getpass("enter your new password:")
                        user.resetPassword(newPassword)

    except ValueError as e:
        print('You must input a number only')
        print("\n")









