import getpass
from accounts import User
user = User()


class UserCredentials:

    def credentials(self):
        self.username = input("Enter username:")
        self.password = getpass.getpass("Enter password: ")
        
        user1 = user.user_exists(self.username,self.password)

        return user1

    def updateUser(self,amount):
        user.update_user(self.username,self.password,amount)

    def resetPassword(self,newPassword):
        user.reset_password(self.username,self.password,newPassword)

    def remainingBalance(self,user1):
        [print(f"remaining balance: {user['balance']}") for user in user1]
        print("\n")
