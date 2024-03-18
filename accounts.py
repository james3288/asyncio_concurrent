from datas import datas

class User:
    listOfUsers:list = []
    def __init__(self):
        self.listOfUsers.extend(datas)

    def user_exists(self,username,password):
        exist = list(filter(lambda x: x['username'] == username and x['password'] == password,self.listOfUsers))
        return exist
    
    def update_user(self,username,password,balance):
        for user in self.listOfUsers:
            if user['username'] == username and user['password'] == password:
                user['balance'] = user['balance'] - balance

    def reset_password(self,username,password,newPassowrd):
        for user in self.listOfUsers:
            if user['username'] == username and user['password'] == password:
                user['password'] = newPassowrd